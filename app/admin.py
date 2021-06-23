from django.contrib import admin

from .models import Book,Product,Category

class CategoryAdmin(admin.ModelAdmin):
  list_display =["title"]
admin.site.register(Category,CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
  list_display = ["category","title"]
admin.site.register(Book,BookAdmin)

class ProductAdmin(admin.ModelAdmin):
  list_display =["name","product_tag"]
admin.site.register(Product,ProductAdmin)