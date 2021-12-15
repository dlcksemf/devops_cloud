from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Tag, Comment, Category
from blog.forms import PostForm


def post_list(request: HttpRequest) -> HttpResponse:
    post_qs = Post.objects.all()
    context = {
        "post_list": post_qs,
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request: HttpRequest, pk:int) -> HttpResponse:
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
            messages.success(request, message="새로 만드는데 성공했습니다.")
            return redirect(saved_post)
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
            saved_post = form.save()
            messages.success(request, message="수정에 성공했습니다.")
            return redirect(saved_post)
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }
    return render(request, "blog/post_form.html", context)


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "삭제에 성공하였습니다.")
        return redirect("blog:post_list")

    context = {
        "post": post,
    }
    return render(request, "post_confirm_delete.html", context)
