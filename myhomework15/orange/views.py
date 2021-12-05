from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from orange.models import Music


def index(request: HttpRequest) -> HttpResponse:
    qs = Music.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    context = { "music_list": qs, }
    return render(request, "orange/index.html", context)


def detail(request: HttpRequest, pk: int) -> HttpResponse:
    music = Music.objects.get(pk=pk)
    context = {"music": music,}
    return render(request, "orange/detail.html", context)