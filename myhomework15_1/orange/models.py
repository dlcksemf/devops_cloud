from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Music(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    released_date = models.DateField()
    description = models.TextField()
    album_cover = models.ImageField(null=True)
    album_cover_thumb = ImageSpecField(
        source="album_cover",
        processors=[ResizeToFill(350, 350)],
        format="JPEG",
        options={"quality": 60},
    )
    korean_music = models.BooleanField(default=True)



