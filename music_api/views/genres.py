from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from music_api.serializers import AlbumSerializer, AlbumSongsSerializer

from music_api.models import Song

class GenreListView(APIView):

    @swagger_auto_schema(
            operation_summary="Get a list of unique genres",
            responses = {
                "200": openapi.Response(
                    description="Genres List",
                    examples = {
                        "application/json": {
                            "genres": [
                                "Genre 1",
                                "Genre 2"
                            ]
                        }
                    }
                )
            }
    )
    def get(self, request, *args, **kwargs):
        """
        Return a list of unique genres
        """
        genres = list(Song.objects.values_list('genre', flat=True).distinct())
        return Response({"genres": genres}, status=status.HTTP_200_OK)