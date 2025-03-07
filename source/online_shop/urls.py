from django.urls import path
from online_shop import views

urlpatterns = [
    path('', views.index, name='products_view'),
    path('products/<int:id>/', views.product_view, name='product_view'),
    path('categories/add/', views.category_add_view, name='category_add_view'),
    path('products/add/', views.product_add_view, name='product_add_view'),
    path('products/delete/<int:id>/', views.delete_product_view, name='delete_product_view'),
    path('categories/', views.categories_view, name='categories_view'),
    path('categories/<int:id>/edit/', views.category_edit_view, name='category_edit_view'),
    path('categories/delete/<int:id>/', views.delete_category_view, name='delete_category_view'),
    path('products/<int:id>/edit/', views.product_edit_view, name='product_edit_view'),
]
