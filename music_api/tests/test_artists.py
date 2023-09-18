from django.test import TestCase
from django.urls import reverse

from rest_framework import status

import json

from music_api.models import Song, Artist, Album

"""
Test class for Artists
"""
class TestArtists(TestCase):
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
    Test artist list
    """
    def test_fetch_artists(self):
        test_url = reverse('artists-list')

        response = self.client.get(test_url)
        artists = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(artists), 2)


    """
    Test fetch 1 artist
    """
    def test_fetch_one_artist(self):
        test_url = reverse(
            'artists-detail',
            kwargs = {'id': 1}
            )
        
        invalid_url = reverse(
            'artists-detail',
            kwargs = {'id': 111}
            )

        response = self.client.get(test_url)
        artist = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(artist['name'], "Artist 1")

        # Test invalid artist
        response2 = self.client.get(invalid_url)
        artist2 = json.loads(response2.content)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(artist2['detail'], 'Not found.')

    """
    Test fetch artist's album
    """
    def test_fetch_artist_album(self):
        test_url = reverse(
            'artists-albums-detail',
            kwargs = {'id': 1},
        )

        response = self.client.get(test_url)
        artist_albums = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(artist_albums['albums']), 1)

    """
    Test fetch artist's album songs
    """
    def test_fetch_artist_album_songs(self):
        test_url = reverse(
            'artists-albums-songs-detail',
            kwargs = {'id': 1},
        )

        response = self.client.get(test_url)
        artist_albums_songs = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(artist_albums_songs['albums']), 1)
        self.assertEqual(len(artist_albums_songs['albums'][0]['songs']), 2)