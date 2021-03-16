import json

import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config

from .permissions import IsAdmin
from .serializers import *


class CooperationRequestView(APIView):
    def post(self, request):
        if request.data['key'] != config('SHOP_SECRET_KEY'):
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        try:
            f = Factory.objects.get(title=request.data['factory'])
        except Factory.DoesNotExist or KeyError:
            return Response('Factory does not exist')
        if f.category_choicer != request.data['category']:
            return Response('It is impossible to cooperate because of category')

        s, created = ShopTitle.objects.get_or_create(title=request.data['shop'])

        try:
            queryset = []
            for product in json.loads(request.data['products']):
                if (product['quantity'] < 1) or (f.available - product['quantity'] < 0):
                    for elem in queryset:
                        elem.delete
                    return Response('It is too much')

                p, created = Product.objects.get_or_create(title=product['title'])

                d, created = DeliveryRequest.objects.get_or_create(shop=s, factory=f, product=p,
                                                                   quantity=product['quantity'])
                f.save()
                queryset.append(d)

        except KeyError:
            return Response('KeyError', status=status.HTTP_400_BAD_REQUEST)

        serializer = DeliveryRequestSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


def delivering():
    for s in ShopTitle.objects.all():
        queryset = []
        for dr in DeliveryRequest.objects.filter(shop=s):
            d = {'title': dr.product.title,
                 'quantity': dr.quantity * dr.queue}
            queryset.append(d)

        data = {'key': config('SHOP_SECRET_KEY'),
                'shop': s.title,
                'products': json.dumps(queryset)}
        try:
            r = requests.post('http://localhost:80/api/shop/delivery/',
                              data=data)
            for dr in DeliveryRequest.objects.filter(shop=s):
                dr.queue = 1
                dr.save()
            return Response(data, status=status.HTTP_201_CREATED)
        except OSError:
            for dr in DeliveryRequest.objects.filter(shop=s):
                dr.queue += 1
                dr.save()
            return Response('Shop does not answer', status=status.HTTP_503_SERVICE_UNAVAILABLE)


class DeliveryView(APIView):

    def post(self, request):
        if request.data['key'] != config('SECRET_KEY'):
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        for s in ShopTitle.objects.all():
            queryset = []
            for dr in DeliveryRequest.objects.filter(shop=s):
                d = {'title': dr.product.title,
                     'quantity': dr.quantity * dr.queue}
                queryset.append(d)

            data = {'key': config('SHOP_SECRET_KEY'),
                    'shop': s.title,
                    'products': json.dumps(queryset)}
            try:
                r = requests.post('http://172.18.0.1:80/api/shop/delivery/',
                                  data=data)
                for dr in DeliveryRequest.objects.filter(shop=s):
                    dr.queue = 1
                    dr.save()
                return Response(
                    DeliveryRequestSerializer(DeliveryRequest.objects.all(), context={'request': request}, many=True).data,
                    status=status.HTTP_201_CREATED)
            except OSError:
                for dr in DeliveryRequest.objects.filter(shop=s):
                    dr.queue += 1
                    dr.save()
                return Response(
                    DeliveryRequestSerializer(DeliveryRequest.objects.all(), context={'request': request}, many=True).data,
                    status=status.HTTP_503_SERVICE_UNAVAILABLE)
