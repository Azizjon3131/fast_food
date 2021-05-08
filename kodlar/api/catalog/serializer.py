from rest_framework import serializers
from catalog.models import Category,Product,Product_type,Product_image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Product_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price','category','product_type']

class Product_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_image
        fields = '__all__'
