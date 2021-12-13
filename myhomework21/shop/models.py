from django.core.validators import RegexValidator
from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamped):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

class Shop(TimeStamped):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    telephone = models.CharField(max_length=13,
                                 validators=[RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$",
                                                           message="전화번호를 입력해주세요")],
                                 help_text="예시) 042-1234-1234")
    description = models.TextField(blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self) -> str:
        return self.name


class Tag(TimeStamped):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name