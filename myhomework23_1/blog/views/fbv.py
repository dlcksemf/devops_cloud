from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Post, Tag, Comment
from blog.forms import PostForm


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
            messages.success(request, message="성공적으로 만들어졌습니다")
            return redirect(saved_post)
    else:
        form = PostForm()

    context = {
        "form": form,
    }
    return render(request, "blog/post_form.html", context)


def post_edit(request: HttpRequest, pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, message=f"[{pk}] 성공적으로 수정되었습니다")
            return redirect(saved_post)
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
    }
    return render(request, "blog/post_form.html", context)


def post_delete(request, pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, message="삭제에 성공했습니다.")
        return redirect("blog:post_list")

    context = {
        "post": post,
    }
    return render(request, "blog/post_confirm_delete.html", context)

