from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Movies(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=20)
    actors = models.CharField(max_length=30)
    comments = models.TextField()
    poster_file = models.ImageField()
    poster_file_thumb = ImageSpecField(
        source="poster_file",
        processors=[ResizeToFill(400, 800)],
        format="JPEG",
        options={"quality": 60},
    )
    created_at = models.DateTimeField(auto_now_add=True)
