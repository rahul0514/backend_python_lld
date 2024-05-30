from ecomapp.models import Product, DiaryProduct
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name']  checking for single validation


class DiaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryProduct
        fields = '__all__'

