import json

import requests
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status

from decouple import config
from .serializers import *
from .models import *
from .permissions import *


class CustomPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 30


class ShopListView(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all().order_by('-title')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination


class ProductInShopView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get(self, request, shop_pk):
        try:
            s = Shop.objects.get(pk=shop_pk)
        except Shop.DoesNotExist:
            return Response("Shop Does Not Exist", status=status.HTTP_404_NOT_FOUND)
        serializer = ProductMPSerializer(Product.objects.filter(shop=s).order_by('-title'),
                                         context={'request': request},
                                         many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, shop_pk, product_pk):
        try:
            serializer = ProductSerializer(Product.objects.get(pk=product_pk),
                                           context={'request': request})
        except Product.DoesNotExist:
            return Response("Product Does Not Exist", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)


class CartListView(APIView):
    permission_classes = [IsOwner]
    pagination_class = CustomPagination

    def get(self, request):
        cart, created = Cart.objects.get_or_create(owner=request.user)
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            p = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response("Product Does Not Exist", status=status.HTTP_404_NOT_FOUND)
        if not p.moderated:
            return Response('U can\'t add this product right now', status=status.HTTP_400_BAD_REQUEST)
        c, created = Cart.objects.get_or_create(owner=request.user)
        if c.current_shop == '' or c.current_shop == p.shop.title:
            try:
                cp, created = CartProduct.objects.get_or_create(main_product=p,
                                                                quantity=request.data['quantity'],
                                                                cart=c)
                c.current_shop = cp.main_product.shop.title
                c.save()
            except KeyError:
                return Response('Add quantity to ur request', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(f'U tried to steal products from {c.current_shop}. U r banned',
                            status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
        serializer = CartSerializer(c, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteFromCartView(APIView):
    permission_classes = [IsOwner]

    def delete(self, request, cp_pk):
        try:
            cp = CartProduct.objects.get(pk=cp_pk)
        except CartProduct.DoesNotExist:
            return Response("CartProduct Does Not Exist", status=status.HTTP_404_NOT_FOUND)
        cp.delete()
        serializer = CartSerializer(cp.cart, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClearCartView(APIView):
    permission_classes = [IsOwner]

    def delete(self, request):
        cart, created = Cart.objects.get_or_create(owner=request.user)
        cart.cartproduct_set.all().delete()
        cart.save()
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchasingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        r = requests.get('http://localhost:80/api/purchase/check_user/', data={'email': request.user.email})
        if r.status_code != 200:
            return Response('create acc, dude', status=status.HTTP_400_BAD_REQUEST)
        c, created = Cart.objects.get_or_create(owner=request.user)
        if c.cartproduct_set.count() == 0:
            return Response('It\'s impossible to purchase nothing', status=status.HTTP_400_BAD_REQUEST)
        queryset = []
        for elem in c.cartproduct_set.all():
            if elem.main_product.quantity < elem.quantity:
                return Response(f'It is not enough {elem.main_product.title} on warehouse',
                                status=status.HTTP_409_CONFLICT)
        sc = ShopCheck.objects.create(customer=request.user, final_price=c.final_price)

        shop = c.cartproduct_set.last().main_product.shop

        for elem in c.cartproduct_set.all():
            elem.main_product.quantity -= elem.quantity
            elem.main_product.save()
            cp = CheckProduct.objects.create(title=elem.main_product.title,
                                             shop_check=sc,
                                             product_pk=elem.main_product.pk,
                                             quantity=elem.quantity)
            queryset.append({'id': cp.product_pk,
                             'title': cp.title,
                             'quantity': cp.quantity})
            elem.delete()

        data = {'key': config('PURCHASE_SECRET_KEY'),
                'email': request.user.email,
                'category': shop.category_choicer,
                'title': shop.title,
                'final_price': sc.final_price,
                'products': json.dumps(queryset)}
        r = requests.post('http://localhost:80/api/purchase/create_purchase/', data=data)

        if r.status_code == 200:
            return Response(data, status=status.HTTP_201_CREATED)
        sc.delete()
        return Response(':(', status=status.HTTP_400_BAD_REQUEST)


class DeliveryOfProductsView(APIView):

    def post(self, request):
        try:
            print('1')
            if request.data['key'] != config('SECRET_KEY'):
                print('2')
                return Response('lol', status=status.HTTP_503_SERVICE_UNAVAILABLE)
            data = json.loads(request.data['products'])
            try:
                s = Shop.objects.get(title=request.data['shop'])
            except Shop.DoesNotExist:
                return Response("Shop Does Not Exist", status=status.HTTP_404_NOT_FOUND)
            queryset = []
            for product in data:
                p, created = Product.objects.get_or_create(title=product['title'],
                                                           shop=s)
                p.quantity += product['quantity']
                p.save()
                queryset.append(p)
        except KeyError:
            return Response('Add all info to ur request', status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ModerateProductView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request, pk):
        serializer = ProductSerializer(Product.objects.filter(moderated=False), context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            p = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response("Product Does Not Exist", status=status.HTTP_404_NOT_FOUND)
        if p not in Product.objects.filter(moderated=False):
            return Response('its already moderated', status=status.HTTP_400_BAD_REQUEST)
        try:
            p.description = request.data['description']
            p.price = request.data['price']
        except KeyError:
            return Response('Add all info to ur request', status=status.HTTP_400_BAD_REQUEST)
        p.moderated = True
        p.save()
        serializer = ProductSerializer(p, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateRequestView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        try:
            r = requests.post('http://localhost:80/api/factory/request/',
                              data={'key': config('SECRET_KEY'),
                                    'factory': request.data['factory'],
                                    'shop': request.data['shop'],
                                    'category': request.data['category'],
                                    'products': json.dumps(request.data['products'])})
        except KeyError:
            return Response('Add all info to ur request', status=status.HTTP_400_BAD_REQUEST)
        return Response(status=r.status_code)
