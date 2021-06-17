# coding=utf-8
from django.urls import path
from .views import *

urlpatterns = [
    path('services/categories/<str:category>', ServiceCategories.as_view()),
    path('services/items/<int:category_id>', Services.as_view())
]