from django.contrib import admin
from online_shop.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
