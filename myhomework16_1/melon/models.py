from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Music(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    album_cover_file = models.ImageField(null=True)
    album_cover_file_thumb =  ImageSpecField(
        source="album_cover_file",
        processors=[ResizeToFill(800, 400)],
        format="JPEG",
        options={"quality": 60},
    )
    released_date = models.DateField()
    description = models.TextField()
    korean_music = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

