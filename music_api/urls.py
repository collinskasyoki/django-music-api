"""
URL configuration for music_api project.
"""
# from django.contrib import admin
from django.urls import path, re_path, include

from music_api.views.genres import GenreListView
from music_api.views.artists import ArtistListSet, ArtistDetail, ArtistAlbumDetail, ArtistAlbumSongDetail
from music_api.views.albums import AlbumListSet
from music_api.views.albums import AlbumDetail, AlbumDetailSongs
from music_api.views.songs import SongListSet, SongDetailView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for DRF-YASG
schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        default_version="v1",
        description="A small API to display a bunch of music information",
        # terms_of_service="https://www.yourapp.com/terms/",
        # contact=openapi.Contact(email="contact@yourapp.com"),
        # license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/genres/', GenreListView.as_view(), name='genre-list'),

    path('api/v1/artists/', ArtistListSet.as_view(), name='artists-list'),
    path('api/v1/artists/<int:id>/', ArtistDetail.as_view(), name='artists-detail'),
    path('api/v1/artists/<int:id>/albums/', ArtistAlbumDetail.as_view(), name='artists-albums-detail'),
    path('api/v1/artists/<int:id>/albums/songs/', ArtistAlbumSongDetail.as_view(), name='artists-albums-detail'),

    path('api/v1/albums/', AlbumListSet.as_view(), name='albums-list'),
    path('api/v1/albums/<int:id>/', AlbumDetail.as_view(), name='albums-detail'),
    path('api/v1/albums/<int:id>/songs/', AlbumDetailSongs.as_view(), name='albums-songs-detail'),

    path('api/v1/songs/', SongListSet.as_view(), name='songs-list'),
    path('api/v1/songs/<int:id>', SongDetailView.as_view(), name='songs-detail'),

    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]
