import json

import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status

from decouple import config
from .serializers import *
from .models import *


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CartListView(APIView):

    def get(self, request):
        cart, created = Cart.objects.get_or_create(owner=request.user)
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCartView(APIView):
    def post(self, request, pk):
        p = Product.objects.get(pk=pk)
        if not p.moderated:
            return Response('U can\'t add this product right now', status=status.HTTP_400_BAD_REQUEST)
        c, created = Cart.objects.get_or_create(owner=request.user)
        if c.current_shop == '' or c.current_shop == p.shop.title:
            cp, created = CartProduct.objects.get_or_create(main_product=p,
                                                            quantity=request.data['quantity'],#
                                                            cart=c)
            c.current_shop = cp.main_product.shop.title
            c.save()
        else:
            return Response(f'U tried to steal products from {c.current_shop}. U r banned',
                            status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
        serializer = CartSerializer(c, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteFromCartView(APIView):

    def delete(self, request, cp_pk):
        cp = CartProduct.objects.get(pk=cp_pk)
        cp.delete()
        serializer = CartSerializer(cp.cart, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClearCartView(APIView):

    def delete(self, request):
        cart, created = Cart.objects.get_or_create(owner=request.user)
        cart.cartproduct_set.all().delete()
        cart.save()
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchasingView(APIView):

    def post(self, request):
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
            cps = CheckProductSerializer(cp, context={'request': request})
            queryset.append(cps.data)
            elem.delete()

        data = {'email': request.user.email,
                'category': shop.category_choicer,
                'title': shop.title,
                'final_price': sc.final_price,
                'products': queryset}
        r = requests.post('http://localhost:8001/api/purchase/create_purchase/', data=data)
        if r.status_code == 400:
            return Response(':(', status=status.HTTP_400_BAD_REQUEST)
        return Response('Все ок', status=status.HTTP_201_CREATED)


class DeliveryOfProductsView(APIView):

    def post(self, request):
        if request.data['key'] != config('SECRET_KEY'):
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        data = json.loads(request.data['products'])#
        s = Shop.objects.get(title=request.data['shop'])#
        queryset = []
        for product in data:
            p, created = Product.objects.get_or_create(title=product['title'],#
                                                       shop=s)
            p.quantity += product['quantity']
            p.save()
            queryset.append(p)
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ModerateProductView(APIView):
    def get(self, request, pk):
        serializer = ProductSerializer(Product.objects.filter(moderated=False), context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        p = Product.objects.get(pk=pk)
        if not p in Product.objects.filter(moderated=False):
            return Response('its already moderated', status=status.HTTP_400_BAD_REQUEST)
        p.description = request.data['description']#
        p.price = request.data['price']#
        p.moderated = True
        p.save()
        serializer = ProductSerializer(p, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
