# Generated by Django 4.2.5 on 2023-09-16 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='albums', to='music_api.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='songs', to='music_api.album'),
        ),
    ]