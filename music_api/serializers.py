from rest_framework import serializers

from .models import Artist, Album, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "title", "artist", "length"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "album_name", "artist_name" "genre", "year", "length", "bitrate", "lyrics", "album", "artist"]
