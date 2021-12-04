from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    released_date = models.DateTimeField()
    description = models.TextField()
    album_cover = models.ImageField(null=True)
    korean_music = models.BooleanField(null=True)



