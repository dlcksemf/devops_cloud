from django.core.validators import RegexValidator
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


class Shop(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    telephone = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                r"^\d{3,4}-?\d{3,4}-?\d{4}$"
            )
        ]
    )
    tag_set = models.ManyToManyField("Tag", blank=True)

    def get_absolute_url(self):
        return reverse("shop:shop_detail", args=[self.pk])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Comment(TimeStampedModel):
    post = models.ForeignKey(Shop, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        ordering = ["-id"]


class Tag(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]