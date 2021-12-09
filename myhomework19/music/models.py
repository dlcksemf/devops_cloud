from django.core.validators import MinLengthValidator
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Music(TimeStamped):
    title = models.CharField(max_length=50, db_index=True)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    album_cover_file = models.ImageField(null=True)
    album_cover_file_thumb = ImageSpecField(
        source="album_cover_file",
        processors=[ResizeToFill(400, 400)],
        format="JPEG",
        options={"quality": 60},
    )
    released_date = models.DateField()
    description = models.TextField(
        validators=[
            MinLengthValidator(3),
        ],
    )
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title


class Comment(TimeStamped):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()


class Tag(TimeStamped):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


