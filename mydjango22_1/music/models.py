from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Music(TimeStamped):
    title = models.CharField(max_length=50, db_index=True)
    artist = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


class Category(TimeStamped):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Tag(TimeStamped):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]