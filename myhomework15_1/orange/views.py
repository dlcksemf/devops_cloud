from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from orange.models import Music


def index(request: HttpRequest) -> HttpResponse:
    qs = Music.objects.all()
    context = {
        "music_list": qs,
    }
    return render(request, "orange/music_index.html", context,)


def detail(request: HttpRequest, pk:int) -> HttpResponse:
    music = Music.objects.get(pk=pk)
    context = {
        "music": music,
    }
    return render(request, "orange/music_detail.html", context,)