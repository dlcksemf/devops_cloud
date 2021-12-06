from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from melon.models import Music


def music_list(request: HttpRequest) -> HttpResponse:
    qs = Music.objects.all()
    context = {"music_list": qs}
    return render(request, "melon/list.html", context)


def music_detail(request: HttpRequest, pk: int) -> HttpResponse:
    music = Music.objects.get(pk=pk)
    context = { "music": music }
    return render(request, "melon/detail.html", context)