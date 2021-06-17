from rest_framework import serializers
from .models import *


class ImageReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageReview
        exclude = ('category',)


class VideoReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoReview
        exclude = ('category',)
