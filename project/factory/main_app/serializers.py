from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Factory
        fields = ('id', 'title', 'category_choicer',)


class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = DeliveryRequest
        fields = ('product', 'quantity')
