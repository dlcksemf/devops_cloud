from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from blog.models import Post, Comment, Tag, Category, Subscriber
from blog.forms import PostForm, CommentForm, SubscriberForm


def post_list(request: HttpRequest) -> HttpResponse:
    post_qs = Post.objects.all()

    format = request.GET.get("format", "")

    if format == "xlsx":
        tabular_data = Post.get_tabular_data(post_qs, format="xlsx")
        return HttpResponse(tabular_data, content_type="application/vnd.ms-excel")
    elif format == "json":
        tabular_data = Post.get_tabular_data(post_qs, format="json")
        return HttpResponse(tabular_data, content_type="application/json")

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
            return redirect(saved_post)
            # return redirect("blog:post_detail", saved_post.pk)
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
    # GET 요청 : 정말 삭제르 할 것인지, 한 번 더 물어봅니다.
    # POST 요청 : 삭제를 하고, 다른 주소로 이동을 시킵니다.
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete() # 실제로 DB에 DELETE 쿼리 실행
        messages.success(request, f"#{pk} 포스팅을 삭제했습니다.")
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {
        "post": post,
    })


def comment_new(request: HttpRequest) -> HttpResponse:
    raise NotImplementedError("comment_new / 아직 구현하지 않았습니다.")


def comment_edit(request: HttpRequest) -> HttpResponse:
    raise NotImplementedError("comment_edit / 아직 구현하지 않았습니다.")


subscriber_new = CreateView.as_view(
    model=Subscriber,
    form_class=SubscriberForm
)