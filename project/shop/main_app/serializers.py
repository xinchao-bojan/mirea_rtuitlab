from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        depth = 1
        fields = ('final_price', 'owner', 'cartproduct_set',)


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = CartProduct
        fields = '__all__'


class CheckProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = CheckProduct
        fields = ('title', 'id', 'quantity',)
