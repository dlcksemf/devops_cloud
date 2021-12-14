from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from music.models import Music, Category, Tag
from music.forms import MusicForm


def music_list(request: HttpRequest) -> HttpResponse:
    qs = Music.objects.all()
    category_qs = Category.objects.all()

    context = {
        "music_list": qs,
        "category_list": category_qs,
    }
    return render(request, "music/music_list.html", context)




