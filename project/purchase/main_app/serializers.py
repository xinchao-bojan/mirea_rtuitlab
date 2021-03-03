from rest_framework import serializers

from .models import *


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        depth = 1
        fields = ['owner', 'final_price', 'purchaseproduct_set', 'category', 'pm_choicer']


class PurchaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
