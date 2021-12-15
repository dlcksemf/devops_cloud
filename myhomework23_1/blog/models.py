from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


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
            ("P", "Post")
        ],
        db_index=True,
        default="D",
    )

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.pk])

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Tag(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.post} // {self.message}"
