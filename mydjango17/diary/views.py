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
    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()
    context = {"post": post,
               "comment_list": comment_list,
               "tag_list": tag_list,
               }
    return render(request, "diary/post_detail.html", context)


def tag(request:HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "diary/tag_list.html", context)