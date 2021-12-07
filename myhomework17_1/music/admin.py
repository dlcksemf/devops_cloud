from django.contrib import admin
from music.models import Music, Comment, Tag

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
