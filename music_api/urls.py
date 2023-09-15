"""
URL configuration for music_api project.
"""
# from django.contrib import admin
from django.urls import path
from .views import ArtistViewSet, AlbumViewSet, SongViewSet

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/artists/', ArtistViewSet.as_view(), name='artists-list'),

    path('api/v1/albums/', AlbumViewSet.as_view(), name='albums-list')
]
