from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from diary.forms import PostForm
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


def tag_detail(request:HttpRequest, tag_name:str ) -> HttpResponse:
    qs = Post.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    context = {"post_list": qs}
    return render(request, "diary/tag_detail.html", context)


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("diary:post_list")
    else:
        form = PostForm()

    return render(request, "diary/post_form.html", {
        "form": form,
    })


def post_edit(request: HttpRequest, pk:int) -> HttpResponse:
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "데이터 저장에 성공했습니다.")
            return redirect("diary:post_list")

    else:
        form = PostForm(instance=post)

    return render(request, "diary/post_form.html", {
        "form": form,
    })