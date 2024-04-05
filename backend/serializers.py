from rest_framework import serializers

from backend.models import Product, Category, CategoryClient
from rest_framework.generics import ListAPIView


class ProductSerializer(serializers.ModelSerializer):
    idcategory = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryClient
        fields = '__all__'


class ProductViewSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='idcategory.name')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'price_iva', 'state_iva', 'state', 'category_name']