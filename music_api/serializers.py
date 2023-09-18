from rest_framework import serializers

from .models import Artist, Album, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "title", "artist", "genre", "length"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "album_name", "artist_name", "genre", "year", "length", "bitrate", "lyrics", "album", "artist"]

class AlbumSongsSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ["id", "title", "artist", "genre", "length", "songs"]


class ArtistAlbumsSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ["id", "name", "albums"]


class ArtistAlbumsSongsSerializer(serializers.ModelSerializer):
    albums = AlbumSongsSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ["id", "name", "albums"]
