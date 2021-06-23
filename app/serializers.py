from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Book,Category,Product

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = (
      "id",
      "title"
      )


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = (
    "id",
      "title",
        "category",
        "author",
          "isbn",
            "pages",
              "price",
                "description", 
                  "imageUrl",
                    "stock",
                      "date_created"
    )

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      "id",
      "product_tag",
      "name",
      "category",
      "price",
      "description", 
      "imageUrl",
      "status",
      "date_created"
    )