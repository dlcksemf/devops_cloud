from django.db import models
import datetime


class Post(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=20)
    actors = models.CharField(max_length=30, blank=True)
    watched_date = models.DateField(default=datetime.date.today)
    rates = models.CharField(max_length=2, blank=True)
    content = models.TextField(blank=True)
    poster = models.ImageField(blank=True)
    created_at = models.DateField(auto_now_add=True)


