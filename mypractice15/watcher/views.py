from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from watcher.models import Movie


def movie_mainscreen(request: HttpRequest) -> HttpResponse:
    return render(request, "watcher/movie_main.html", {})


def movie_list(request: HttpRequest) -> HttpResponse:
    qs = Movie.objects.all()
    context = {"movie_list": qs, }
    return render(request, "watcher/movie_list.html", context)


def movie_detail(request: HttpRequest) -> HttpResponse:
    return render(request, "watcher/movie_detail.html", {})
