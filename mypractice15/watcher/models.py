from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=70)
    actor = models.CharField(max_length=70)
    comment = models.TextField(blank=True)
    poster_file = models.ImageField()
    poster_thumb = ImageSpecField(
        source="poster_file",
        processors=[ResizeToFill(200, 400)],
        format="JPEG",
        options={"quality": 60},
    )
    # TODO : add watched date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    watched = models.BooleanField()