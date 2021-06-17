# coding=utf-8
from django.urls import path
from .views import *

urlpatterns = [
    path('order/', CreateOrderView.as_view()),
    path('application/', ApplicationCreate.as_view()),
]