from django.contrib import admin
from music.models import Music, Comment, Tag


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["title", "album_cover_file"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["content"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]