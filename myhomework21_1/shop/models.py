from django.core.validators import RegexValidator
from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamped):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Shop(TimeStamped):
    name = models.CharField(max_length=200, db_index=True)
    telephone = models.CharField(max_length=15, validators=[
        RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="정확한 전화번호를 입력하세요."),
    ],
                                 help_text="입력 예 : 010-0000-0000")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Tag(TimeStamped):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

