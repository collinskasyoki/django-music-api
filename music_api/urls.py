"""
URL configuration for music_api project.
"""
# from django.contrib import admin
from django.urls import path, re_path, include

from music_api.views.artists import ArtistListSet
from music_api.views.albums import AlbumListSet
from music_api.views.songs import SongListSet

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
    path('api/v1/artists/', ArtistListSet.as_view(), name='artists-list'),

    path('api/v1/albums/', AlbumListSet.as_view(), name='albums-list'),

    path('api/v1/songs/', SongListSet.as_view(), name='songs-list'),

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
