
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('list', views.GetVideosView.as_view(), name = 'list'),
    path('search', views.SearchVideosView.as_view(), name = 'search'),
]
