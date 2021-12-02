from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=20)
    actors = models.CharField(max_length=30)
    comments = models.TextField()
    poster_file = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)