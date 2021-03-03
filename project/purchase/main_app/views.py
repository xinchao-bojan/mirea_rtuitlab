from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import status

from .serializers import *
from .models import *


class CreatePurchaseView(APIView):
    def post(self, request):
        c, created = Category.objects.get_or_create(title=request.data['category'])
        try:
            u = CustomUser.objects.get(email=request.data['email'])
        except CustomUser.DoesNotExist:
            return Response('Дядя, создай тут акк перед тем, как юзать сервис', status=status.HTTP_400_BAD_REQUEST)
        p = Purchase.objects.create(owner=u,
                                    title=request.data['title'],
                                    final_price=request.data['final_price'],
                                    category=c)

        for elem in request.data['products']:
            PurchaseProduct.objects.create(title=elem['title'],
                                           purchase=p,
                                           product_pk=elem['id'],
                                           quantity=elem['quantity'])
        serializer = PurchaseSerializer(p, context={'request': request})
        return Response(status=status.HTTP_200_OK)


class PurchaseListView(APIView):
    def get(self, request):
        serializer = PurchaseSerializer(Purchase.objects.filter(owner=request.user).order_by('category__title'),
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)


class UpdatePurchaseView(APIView):
    def get(self, request, pk):
        serializer = PurchaseSerializer(Purchase.objects.get(pk=pk), context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        p = Purchase.objects.get(pk=pk)
        if 'category' in request.data:
            try:
                p.category = Category.objects.get(title=request.data['category'])
            except Category.DoesNotExist:
                return Response('u should create category before adding', status=status.HTTP_418_IM_A_TEAPOT)
        if 'payment' in request.data:
            p.pm_choicer = request.data['payment']
        p.save()
        serializer = PurchaseSerializer(p, context={'request': request})
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)


class CreateCategoryView(APIView):
    def post(self, request):
        c, created = Category.objects.get_or_create(title=request.data['title'])
        if created:
            return Response(f'Категория {c.title} успешно создана', status=status.HTTP_201_CREATED)
        return Response(f'Категория {c.title} была создана ранее', status=status.HTTP_400_BAD_REQUEST)
