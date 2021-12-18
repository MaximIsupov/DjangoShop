from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ProductSerializer, CategorySerializer, ImgSerializer
from Shop.models import Product, Category, Img


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ImgViewSet(viewsets.ModelViewSet):
    queryset = Img.objects.all()
    serializer_class = ImgSerializer
