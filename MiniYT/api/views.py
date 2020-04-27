from django.shortcuts import render
from data.models import Video
from data.serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.contrib.postgres.search import SearchQuery

class GetVideosView(ListAPIView):
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Video.objects.all().order_by('-publishedAt')

class SearchVideosView(ListAPIView):
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        searchQuery = self.request.GET.get('query')
        queryset = Video.objects.filter(searchvector = SearchQuery(searchQuery, config='english')).order_by('-publishedAt')
        return queryset