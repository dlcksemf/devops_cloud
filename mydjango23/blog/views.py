from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment, Tag, Category
from blog.forms import PostForm, CommentForm


def post_list(request: HttpRequest) -> HttpResponse:
    post_qs = Post.objects.all()
    context = {
        "post_list": post_qs,
    }

    return render(request, "blog/post_list.html", context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post": post,
    }

    return render(request, "blog/post_detail.html", context)


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, "새로운 포스팅을 저장했습니다.")
            return redirect("blog:post_detail", saved_post.pk)
    else:
        form = PostForm()
    context = {
     "form": form,
    }

    return render(request, "blog/post_form.html", context)


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f"#{pk} 포스팅을 저장했습니다.")
            return redirect("blog:post_detail", pk)
    else:
        form = PostForm(instance=post)
    context = {
        "form": form,
        "post": post,
    }

    return render(request, "blog/post_form.html", context)


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    raise NotImplementedError("삭제는 아직 강의에서 다루지 않았습니다.")


def comment_new(request: HttpRequest) -> HttpResponse:
    raise NotImplementedError("comment_new / 아직 구현하지 않았습니다.")


def comment_edit(request: HttpRequest) -> HttpResponse:
    raise NotImplementedError("comment_edit / 아직 구현하지 않았습니다.")