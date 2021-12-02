from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from movies.models import Movies


def index(request: HttpRequest) -> HttpResponse:
    qs = Movies.objects.all()
    return render(
        request,
        "movies/index.html",
        {
            "movies_list": qs,
        },
    )


def movies_review(request: HttpRequest, pk: int) -> HttpResponse:
    movie = Movies.objects.get(pk=pk)
    return render(
        request,
        "movies/movies_review.html",
        {
            "movies": movie,
        },
    )
