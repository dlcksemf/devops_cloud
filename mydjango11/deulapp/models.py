from django.db import models

class Userinfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="이름")
    address = models.CharField(max_length=100, verbose_name="주소")
    gen = (
        ("강아지", "강아지"),
        ("고양이", "고양이"),
    )
    prefer_animal = models.CharField(
        max_length=3, choices=gen, verbose_name="좋아하는 동물", default=""
    )