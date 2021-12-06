from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Music(models.Model):
    title = models.CharField(max_length=30,db_index=True)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    released_date = models.DateField()
    description = models.TextField()
    album_cover_file = models.ImageField(null=True)
    album_cover_file_thumb = ImageSpecField(
        source="album_cover_file",
        processors=[ResizeToFill(400, 400)],
        format="JPEG",
        options={"quality": 60},
    )
    korean_music = models.BooleanField()