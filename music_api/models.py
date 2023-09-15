from django.db import models

class Artist:
    name = models.CharField(200)


class Album:
    name = models.CharField(200)
    albumartist = models.ForeignKey(Artist, on_delete=models.RESTRICT, on_update=models.CASCADE)


class Song:
    title = models.CharField(300)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT, on_update=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, on_update=models.CASCADE, null=True)
    length = models.IntegerField()
    year = models.SmallIntegerField()
    genre = models.CharField(100)
    lyrics = models.TextField(null=True)