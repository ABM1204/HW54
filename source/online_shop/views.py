from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from online_shop.models import Product, Category

def index(request):
    products = Product.objects.all()
    return render(request, 'products_view.html', {'products': products})

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_view.html', {'product': product})

def category_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if not name:
            return HttpResponseBadRequest('Name cannot be empty')

        category = Category(name=name, description=description)
        category.save()
        return redirect('products_view')

    return render(request, 'add_category.html')

def product_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        image_url = request.POST.get('image_url')

        if not name:
            return HttpResponseBadRequest('Name cannot be empty')

        if not category_id:
            return HttpResponseBadRequest('Category cannot be empty')

        if not price:
            return HttpResponseBadRequest('Price cannot be empty')

        if not image_url:
            return HttpResponseBadRequest('Image URL cannot be empty')

        category = get_object_or_404(Category, id=category_id)

        product = Product(name=name, description=description, category=category, price=price, image=image_url)
        product.save()
        return redirect('products_view')

    categories = Category.objects.all()
    return render(request, 'add_product.html', {'categories': categories})
