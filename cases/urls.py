# coding=utf-8
from django.urls import path
from .views import *

urlpatterns = [
    path('cases/<str:category>', Cases.as_view()),
    path('cases/', Cases.as_view())
]