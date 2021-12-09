from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from music.forms import MusicForm
from music.models import Music, Comment, Tag


def music_list(request: HttpRequest) -> HttpResponse:
    qs = Music.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)
    context = {"music_list": qs}
    return render(request, "music/music_list.html", context)


def music_detail(request: HttpRequest, pk:int) -> HttpResponse:
    music = Music.objects.get(pk=pk)
    comment_list = music.comment_set.all()
    tag_list = music.tag_set.all()

    context = {"music": music,
               "tag_list": tag_list,
               "comment_list": comment_list }
    return render(request, "music/music_detail.html", context)


def tag_detail(request: HttpRequest, tag_name:str) -> HttpResponse:
    qs = Music.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    context = {"tag_name": tag_name,
               "music_list": qs}
    return render(request, "music/tag_detail.html", context)


def music_new(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.released_date = "2002-03-25"
            music.save()
            return redirect("music:music_list")
    else:
        form = MusicForm()

    return render(request, "music/music_form.html", {"form": form})


def music_edit(request:HttpRequest, pk:int) -> HttpResponse:
    music = Music.objects.get(pk=pk)
    if request.method == "POST":
        form = MusicForm(request.POST, request.FILES, instance=music)
        if form.is_valid():
            form.save()
            return redirect("music:music_list")
    else:
        form = MusicForm(instance=music)

    return render(request, "music/music_form.html", {"form": form})
