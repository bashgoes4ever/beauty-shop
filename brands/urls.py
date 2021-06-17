# coding=utf-8
from django.urls import path
from .views import *

urlpatterns = [
    path('brands/<str:category>', Brands.as_view()),
    path('brands/', Brands.as_view())
]