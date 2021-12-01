from django.db import models
from blog.upload_to import uuid_name_upload_to


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # upload_to
    # 저장 할 때 불러짐
    # - 문자열 : 파일이 저장되는 폴더의 경로 (일자별로 폴더 생성해서 구분)
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
