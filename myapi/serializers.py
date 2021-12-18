from Shop.models import Product, Category, Img
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'imgs',
            'category_name',
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]


class ImgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Img
        fields = [
            'alt',
            'src',
        ]