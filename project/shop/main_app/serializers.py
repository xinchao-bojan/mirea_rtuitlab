from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = '__all__'


class ProductMPSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = ('id', 'title',)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        depth = 2
        fields = ('id', 'final_price',  'cartproduct_set',)


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = CartProduct
        fields = '__all__'


class CheckProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = CheckProduct
        fields = ('id', 'title', 'id', 'quantity',)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Shop
        fields = ('id', 'title', 'category_choicer')
