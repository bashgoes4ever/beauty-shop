# coding=utf-8
from django.urls import path
from .views import *

urlpatterns = [
    path('shop/categories/', ProductCategories.as_view()),
    path('shop/products/<int:category_id>', Products.as_view()),
    path('shop/products/home/', ProductsHome.as_view()),
]