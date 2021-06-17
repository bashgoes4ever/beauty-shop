from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class Masters(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category=None):
        if category:
            objs = Master.objects.filter(category=category)
        else:
            objs = Master.objects.all()
        serializer = MasterSerializer(objs, many=True)
        return Response(serializer.data)

