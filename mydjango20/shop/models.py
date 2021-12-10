from django.core.validators import RegexValidator
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Shop(TimeStampedModel):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=14,
                                 validators=[
                                     RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="전화번호를 입력해주세요."),
                                 ],
                                 help_text="입력예) 042-1234-1234")
    tag_set = models.ManyToManyField('Tag', blank=True)


class Review(TimeStampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)