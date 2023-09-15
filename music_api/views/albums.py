from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from music_api.serializers import ArtistSerializer, AlbumSerializer, SongSerializer

from music_api.models import Artist, Album, Song


class AlbumListSet(APIView):

    @swagger_auto_schema(
            operation_summary="List all albums",
            responses={200: openapi.Response("List of albums", AlbumSerializer(many=True))}
    )
    def get(self, request, *args, **kwargs):
        # Filter options?

        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


