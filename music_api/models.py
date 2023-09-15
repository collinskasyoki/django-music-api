from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)


class Album(models.Model):
    name = models.CharField(max_length=200)
    albumartist = models.ForeignKey(Artist, on_delete=models.RESTRICT)


class Song(models.Model):
    title = models.CharField(max_length=300)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT)
    length = models.IntegerField()
    year = models.SmallIntegerField()
    genre = models.CharField(max_length=100)
    lyrics = models.TextField(null=True)