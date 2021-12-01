from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=20)
    review = models.TextField()
    watched_date = models.DateField()
