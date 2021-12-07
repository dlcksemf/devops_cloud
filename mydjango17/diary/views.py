from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from diary.models import Post, Comment, Tag


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    query = request.GET.get("query", "")

    if query:
        qs = qs.filter(title__icontains=query)

    context = {"post_list": qs,}
    return render(request, "diary/post_list.html", context)


def post_detail(request:HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    context = {"post": post,}
    return render(request, "diary/post_detail.html", context)