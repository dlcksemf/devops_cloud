from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from melon.models import Music


def melon_list(request: HttpRequest) -> HttpResponse:
    qs = Music.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    context = { "music_list": qs }
    return render(request, "melon/index.html", context)


def melon_detail(request: HttpRequest, pk:int) -> HttpResponse:
    music = Music.objects.get(pk=pk)
    context = { "music": music }
    return render(request, "melon/detail.html", context)

