from django.urls import path
from online_shop import views

urlpatterns = [
    path('', views.index, name='products_view'),
    path('products/<int:id>/', views.product_view, name='product_view'),
    path('categories/add/', views.category_add_view, name='category_add_view'),
    path('products/add/', views.product_add_view, name='product_add_view')
]