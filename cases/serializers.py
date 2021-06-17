from rest_framework import serializers
from .models import *


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        exclude = ('category',)
