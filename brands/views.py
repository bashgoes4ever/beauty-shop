from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class Brands(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category=None):
        if category:
            objs = Brand.objects.filter(category=category)
        else:
            objs = Brand.objects.all()
        serializer = BrandSerializer(objs, many=True)
        return Response(serializer.data)

