# Generated by Django 4.2.5 on 2023-09-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0002_album_genre_alter_album_artist_alter_song_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]