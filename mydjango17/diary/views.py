from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from diary.models import Post, Comment, Tag


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    context = {"post_list": qs,}

    return render(request, "diary/post_list.html", context)