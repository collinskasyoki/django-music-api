from django.test import TestCase
from django.urls import reverse

from rest_framework import status

import json

from music_api.models import Song, Artist, Album

"""
Test class for Songs
"""
class TestSongs(TestCase):
    def setUp(self):
        test_artist1 = Artist.objects.create(
            id = 1,
            name = "Artist 1",
        )
        test_artist2 = Artist.objects.create(
            id = 2,
            name = "Artist 2",
        )

        test_album1 = Album.objects.create(
            id = 1,
            title = "Album 1",
            artist = test_artist1,
            genre = "Genre 1",
        )
        test_album2 = Album.objects.create(
            id = 2,
            title = "Album 1",
            artist = test_artist2,
            genre = "Genre 1",
        )

        test_song = Song.objects.create(
            id = 1,
            title = "Test Song 1",
            album = test_album1,
            album_name = "Album 1",
            artist = test_artist1,
            artist_name = "Artist 1",
            genre = "Genre 1",
            year = 2000,
            length = 10000,
            bitrate = 320000
        )
        test_song = Song.objects.create(
            id = 2,
            title = "Test Song 2",
            album = test_album1,
            album_name = "Album 1",
            artist = test_artist1,
            artist_name = "Artist 1",
            genre = "Genre 1",
            year = 2000,
            length = 10000,
            bitrate = 320000
        )
        test_song3 = Song.objects.create(
            id = 3,
            title = "Test Song 3",
            album = test_album2,
            album_name = "Album 2",
            artist = test_artist2,
            artist_name = "Artist 2",
            genre = "Genre 3",
            year = 2003,
            length = 10003,
            bitrate = 320000
        )


    """
    Test songs list
    """
    def test_fetch_songs(self):
        test_url = reverse('songs-list')

        response = self.client.get(test_url)
        songs = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(songs['count'], 3)
        self.assertEqual(len(songs['results']), 3)


    """
    Test fetch 1 song
    """
    def test_fetch_one_song(self):
        test_url = reverse(
            'songs-detail',
            kwargs = {'id': 1}
            )
        
        invalid_url = reverse(
            'songs-detail',
            kwargs = {'id': 111}
            )

        response = self.client.get(test_url)
        song = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(song['title'], "Test Song 1")

        # Test invalid artist
        response2 = self.client.get(invalid_url)
        song2 = json.loads(response2.content)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(song2['detail'], 'Not found.')


    """
    Test fetch songs by genre
    """
    def test_fetch_songs_by_genre(self):
        test_url = reverse('songs-list') + '?genre=Genre 1'
        response = self.client.get(test_url)
        songs = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(songs['count'], 2)
        self.assertEqual(len(songs['results']), 2)