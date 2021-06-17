from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class ServiceCategories(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category):
        objs = ServiceCategory.objects.filter(category=category)
        serializer = ServiceCategorySerializer(objs, many=True)
        return Response(serializer.data)


class Services(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category_id):
        objs = Service.objects.filter(category=category_id)
        serializer = ServiceSerializer(objs, many=True)
        return Response(serializer.data)

