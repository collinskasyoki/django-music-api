from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from music_api.serializers import ArtistSerializer, ArtistAlbumsSerializer, ArtistAlbumsSongsSerializer

from music_api.models import Artist, Album, Song


class ArtistListSet(APIView):

    @swagger_auto_schema(
            operation_summary="List all artists",
            responses={200: openapi.Response("List of artists", ArtistSerializer(many=True))}
    )
    def get(self, request, *args, **kwargs):
        # Filter options?

        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArtistDetail(APIView):

    @swagger_auto_schema(
            operation_summary="Get the details of an artist",
            responses={200: openapi.Response("Artist details", ArtistSerializer())}
        )
    def get(self, request, *args, **kwargs):
        """
        Get the details of one artist
        """
        artist = get_object_or_404(Artist, id=kwargs['id'])
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArtistAlbumDetail(APIView):

    @swagger_auto_schema(
            operation_summary="Get the albums of an artist",
            responses={200: openapi.Response("Albums list", ArtistAlbumsSerializer())}
    )
    def get(self, request, *args, **kwargs):
        """
        Get the albums of an artist
        """
        artist = get_object_or_404(Artist, id=kwargs["id"])
        serializer = ArtistAlbumsSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArtistAlbumSongDetail(APIView):

    @swagger_auto_schema(
            operation_summary="Get the albumbs and songs of an artist",
            responses= {200: openapi.Response("Album list", ArtistAlbumsSongsSerializer())}
    )
    def get(self, request, *args, **kwargs):
        """
        Get the albums and songs of an artist
        """
        artist = get_object_or_404(Artist, id=kwargs['id'])
        serializer = ArtistAlbumsSongsSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)