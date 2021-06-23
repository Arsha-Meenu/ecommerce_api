from re import search
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import server_error
from rest_framework.utils.field_mapping import ClassLookupDict
from .serializers import CategorySerializer,BookSerializer,ProductSerializer
from .models import Category, Book,Product

class ListCategory(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class =  CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class ListBook(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class ListProduct(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
  queryset= Product.objects.all()
  serializer_class = ProductSerializer