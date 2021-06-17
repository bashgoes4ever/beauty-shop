from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class Reviews(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category=None):
        if category:
            image_reviews = ImageReview.objects.filter(category=category)
            video_reviews = VideoReview.objects.filter(category=category)
        else:
            image_reviews = ImageReview.objects.all()
            video_reviews = VideoReview.objects.all()
        image_review_serializer = ImageReviewSerializer(image_reviews, many=True)
        video_review_serializer = VideoReviewSerializer(video_reviews, many=True)
        return Response({
            'image_reviews': image_review_serializer.data,
            'video_reviews': video_review_serializer.data
        })

