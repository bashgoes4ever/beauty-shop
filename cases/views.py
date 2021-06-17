from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class Cases(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category=None):
        if category:
            objs = Case.objects.filter(category=category)
        else:
            objs = Case.objects.all()
        serializer = CaseSerializer(objs, many=True)
        return Response(serializer.data)

