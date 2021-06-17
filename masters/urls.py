# coding=utf-8
from django.urls import path
from .views import *

urlpatterns = [
    path('masters/<str:category>', Masters.as_view()),
    path('masters/', Masters.as_view())
]