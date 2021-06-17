from rest_framework import serializers
from .models import *


class MasterSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterSkill
        exclude = ('master',)


class MasterSerializer(serializers.ModelSerializer):
    skills = MasterSkillSerializer(many=True)

    class Meta:
        model = Master
        exclude = ('image',)
