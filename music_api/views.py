from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

from .models import Artist, Album, Song

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

