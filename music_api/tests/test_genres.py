from django.test import TestCase
from django.urls import reverse

from rest_framework import status

import json

from music_api.models import Song, Artist, Album

"""
Test class for Genres
"""
class TestGenre(TestCase):
    def setUp(self):
        test_artist = Artist.objects.create(
            name = "Artist 1",
        )
        test_album = Album.objects.create(
            title = "Album 1",
            artist = test_artist,
            genre = "Genre 1",
        )
        test_song = Song.objects.create(
            title = "Test Song 1",
            album = test_album,
            album_name = "Album 1",
            artist = test_artist,
            artist_name = "Artist 1",
            genre = "Genre 1",
            year = 2000,
            length = 10000,
            bitrate = 320000
        )

    """
    Test genre fetched
    """
    def test_fetch_genre(self):
        test_url = reverse('genre-list')

        response = self.client.get(test_url)
        genre = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(genre['genres'][0], 'Genre 1')
