from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from online_shop.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'products_view.html', {'products': products})

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_view.html', {'product': product})



