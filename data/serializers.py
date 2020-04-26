from rest_framework import serializers, pagination
from .models import Video

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['videoId', 'title', 'description', 'publishedAt', 'thumbnailURL']

class PaginatedVideoSerializer(pagination.PageNumberPagination):

    class Meta:
        object_serializer_class = VideoSerializer