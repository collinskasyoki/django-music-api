from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=300, unique=True)


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, related_name='albums')
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, blank=True, null=True)
    length = models.CharField(max_length=50, blank=True, null=True)


class Song(models.Model):
    title = models.CharField(max_length=300)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT, blank=True, null=True, related_name='songs')
    album_name = models.CharField(max_length=300, db_column='album')
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT)
    artist_name = models.CharField(max_length=300, db_column='artist_name')
    genre = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    length = models.IntegerField()
    bitrate = models.IntegerField()
    lyrics = models.TextField(null=True)