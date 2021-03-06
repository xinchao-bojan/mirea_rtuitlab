import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from decouple import config

from .serializers import *
from .models import *


def getCategory(name, user):
    try:
        c = Category.objects.get(title=name, default=True)
        return c
    except Category.DoesNotExist:
        try:
            c = Category.objects.get(default=False, title=name, owner=user)
            return c
        except Category.DoesNotExist:
            return None


class CreatePurchaseView(APIView):

    def post(self, request):
        try:
            if request.data['key'] != config('SECRET_KEY'):
                return Response('wrong key', status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response('u are not a shop', status=status.HTTP_404_NOT_FOUND)

        try:
            c = getCategory(request.data['category'], request.user)
            if c is None:
                return Response('fix category', status=status.HTTP_400_BAD_REQUEST)
            try:
                u = CustomUser.objects.get(email=request.data['email'])
            except CustomUser.DoesNotExist:
                return Response('Дядя, создай тут акк перед тем, как юзать сервис', status=status.HTTP_400_BAD_REQUEST)
            p = Purchase.objects.create(owner=u,
                                        title=request.data['title'],
                                        final_price=request.data['final_price'],
                                        category=c)
            for elem in json.loads(request.data['products']):
                PurchaseProduct.objects.create(title=elem['title'],
                                               purchase=p,
                                               product_pk=elem['id'],
                                               quantity=elem['quantity'])
            serializer = PurchaseSerializer(p, context={'request': request})
        except KeyError:
            return Response('Add all info to ur request', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchaseByCategoryListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, category):
        c = getCategory(category, request.user)
        if c is None:
            return Response('fix category', status=status.HTTP_400_BAD_REQUEST)
        p = Purchase.objects.filter(category=c).order_by('category__title')
        if not p:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PurchaseSerializer(p,
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)


class PurchaseListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = PurchaseSerializer(Purchase.objects.filter(owner=request.user).order_by('category__title'),
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)


class UpdatePurchaseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            serializer = PurchaseSerializer(Purchase.objects.get(pk=pk, owner=request.user),
                                            context={'request': request})
        except Purchase.DoesNotExist:
            return Response('Purchase Does Not Exist', status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        p = Purchase.objects.get(pk=pk)
        if 'category' in request.data:
            cat = getCategory(request.data['category'], request.user)
            if cat is None:
                return Response('u should create category before adding', status=status.HTTP_418_IM_A_TEAPOT)
            p.category = cat
            p.save()
        if 'payment' in request.data:
            p.pm_choicer = request.data['payment']
        p.save()
        serializer = PurchaseSerializer(p, context={'request': request})
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)


class CreateCategoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            c = getCategory(request.data['title'], request.user)
        except KeyError:
            return Response('Add all info to ur request', status=status.HTTP_400_BAD_REQUEST)

        if c is None:
            c = Category.objects.create(title=request.data['title'], owner=request.user)
            return Response(f'Категория {c.title} успешно создана', status=status.HTTP_201_CREATED)
        return Response(f'Категория {c.title} была создана ранее', status=status.HTTP_400_BAD_REQUEST)


class CheckAuthorization(APIView):
    def get(self, request):
        try:
            CustomUser.objects.get(email=request.data['email'])
            return Response(status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist or KeyError:
            return Response('Add all info to ur request', status=status.HTTP_400_BAD_REQUEST)
