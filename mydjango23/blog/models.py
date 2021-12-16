import tablib
from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Post(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="blog/post/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)
    # FIXME : 장고 3에서 추가된 TextChoices 기능을 활용
    status = models.CharField(
        max_length=1,
        # 셀렉트박스 형식으로 나옴
        choices=[
            ('D', '초안'), # Draft // DB저장값, Label
            ('P', '공개'), # Published
        ],
        db_index=True,
        default='D',
    )

    def __str__(self):
        return self.title

    # post detail 주소 문자열을 반환
    # detail 페이지를 구현하자마자, 즉시 아래 메서드를 구현합니다.

    @classmethod
    def get_tabular_data(cls, queryset, format="xlsx") -> bytes:
        dataset = tablib.Dataset()
        dataset.headers = ["id", "title", "created_at", "updated_at"]
        for post in queryset:
            dataset.append(
                [
                    post.id,
                    post.title,
                    post.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    post.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                ]
            )

        return dataset.export(format)

    class Meta:
        ordering = ["-id"]


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"[{self.post}] / {self.message}"

    class Meta:
        ordering = ["-id"]


class Tag(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

