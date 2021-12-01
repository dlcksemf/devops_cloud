from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from moviereview.models import Post


def index(request):
    return render(request, "moviereview/index.html")


def movie_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    qs = qs.order_by("-pk")

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, "moviereview/movie_list.html",{
        "movie_list": qs,
    })


def post_detail(request: HttpRequest, pk:int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    return render(request, "moviereview/post_detail.html",{
        "post": post
    })