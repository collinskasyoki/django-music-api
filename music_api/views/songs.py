from django.shortcuts import get_object_or_404

from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from music_api.serializers import SongSerializer
from music_api.models import Song


class Pagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'limit'
    max_page_size = 2000
    page_query_param = 'page'


class SongListSet(generics.ListAPIView):

    pagination_class = Pagination

    @swagger_auto_schema(
            operation_summary="List songs",
            responses={200: openapi.Response("List of songs", SongSerializer(many=True))}
    )
    def get(self, request, *args, **kwargs):
        # Filter options?

        queryset = Song.objects.all().order_by('artist', 'album', 'id')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SongSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SongSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SongDetailView(APIView):

    @swagger_auto_schema(
            operation_summary="List one song",
            responses={200: openapi.Response("Song details", SongSerializer())}
    )
    def get(self, request, *args, **kwargs):
        """
        Get details of one song
        """
        queryset = get_object_or_404(Song, id=kwargs['id'])
        serializer = SongSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)