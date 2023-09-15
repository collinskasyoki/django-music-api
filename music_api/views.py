from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

from .models import Artist, Album, Song


class Pagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'limit'
    max_page_size = 2000
    page_query_param = 'page'


class ArtistViewSet(APIView):

    def get(self, request, *args, **kwargs):
        # Filter options?

        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AlbumViewSet(APIView):

    def get(self, request, *args, **kwargs):
        # Filter options?

        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SongViewSet(generics.ListAPIView):

    pagination_class = Pagination

    def get(self, request, *args, **kwargs):
        # Filter options?

        queryset = Song.objects.all().order_by('artist', 'album', 'id')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SongSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SongSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
