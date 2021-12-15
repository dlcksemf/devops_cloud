from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from music.models import Music, Category, Tag
from music.forms import MusicForm


def music_list(request: HttpRequest) -> HttpResponse:
    qs = Music.objects.all()
    category_qs = Category.objects.all()

    category_id = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    context = {
        "music_list": qs,
        "category_list": category_qs,
    }
    return render(request, "music/music_list.html", context)


def music_detail(request: HttpRequest, pk: int) -> HttpResponse:
    music = get_object_or_404(Music, pk=pk)
    tag_list = music.tag_set.all()

    context = {
        "music": music,
        "tag_list": tag_list,
    }
    return render(request, "music/music_detail.html", context)


def music_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            saved_music = form.save()
            return redirect("music:music_detail", saved_music.pk)
    else:
        form = MusicForm()

    return render(request, "music/music_form.html", {
        "form": form,
    })


def music_edit(request: HttpRequest, pk: int) -> HttpResponse:
    music = get_object_or_404(Music, pk=pk)
    if request.method == "POST":
        form = MusicForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect("music:music_detail", music.pk)
    else:
        form = MusicForm(instance=music)

    return render(request, "music/music_form.html", {
        "form": form,
    })

