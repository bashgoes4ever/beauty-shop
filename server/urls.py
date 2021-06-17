from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('brands.urls')),
    path('api/v1/', include('cases.urls')),
    path('api/v1/', include('masters.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('services.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('baskets.urls')),
    path('api/v1/', include('orders.urls'))
]

urlpatterns += [re_path(r'^.*',  include("start.urls"))]