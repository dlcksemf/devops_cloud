from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Post(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="blog/post/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)
    status = models.CharField(
        max_length=1,
        choices=[
            ("D", "Draft"),
            ("P", "Publish"),
        ],
        db_index=True,
        default="D",
    )

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.pk])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["-id"]


class Tag(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]