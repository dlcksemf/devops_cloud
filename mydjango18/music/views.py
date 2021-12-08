from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from music.models import Music, Comment, Tag


def music_list(request:HttpRequest) -> HttpResponse:
    qs = Music.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    context = {"music_list": qs,}
    return render(request, "music/music_list.html", context)


def music_detail(request:HttpRequest, pk:int) -> HttpResponse:
    music = Music.objects.get(pk=pk)
    comment_list = music.comment_set.all()
    tag_list = music.tag_set.all()
    context = {
        "music": music,
        "comment_list": comment_list,
        "tag_list": tag_list,
    }
    return render(request, "music/music_detail.html", context)


def tag_detail(request:HttpRequest, tag_name:str) -> HttpResponse:
    qs = Music.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    context = {"music_list": qs}
    return render(request, "music/tag_detail.html", context)
