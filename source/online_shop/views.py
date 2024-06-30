from django.shortcuts import render
from online_shop.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
