from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from music_api.serializers import AlbumSerializer, AlbumSongsSerializer

from music_api.models import Album


class AlbumListSet(APIView):

    @swagger_auto_schema(
            operation_summary="List albums",
            manual_parameters=[
                openapi.Parameter(
                    name='genre',
                    in_=openapi.IN_QUERY,
                    type=openapi.TYPE_STRING,
                    description='Filter by genre name',
                )
            ],
            responses={200: openapi.Response("List of albums", AlbumSerializer(many=True))}
    )
    def get(self, request, *args, **kwargs):
        genre_filter = request.query_params.get('genre')

        queryset = Album.objects.all()
        if genre_filter:
            queryset = queryset.filter(genre=genre_filter)

        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AlbumDetail(APIView):

    @swagger_auto_schema(
        operation_summary="Retrieve an album by ID",
        responses={200: openapi.Response("Album details", AlbumSerializer())},
    )
    def get(self, request, *args, **kwargs):
        """
        Retrieve an album by its ID
        """

        album = get_object_or_404(Album, pk=kwargs["id"])
        serializer = AlbumSerializer(album)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AlbumDetailSongs(APIView):

    @swagger_auto_schema(
        operation_summary="Retrieve album songs",
        responses={200: openapi.Response("Album songs", AlbumSongsSerializer())})
    def get(self, request, *args, **kwargs):
        """"
        Retrieve album songs by ID
        """
        album = get_object_or_404(Album, pk=kwargs["id"])
        serializer = AlbumSongsSerializer(album)
        return Response(serializer.data, status=status.HTTP_200_OK)
