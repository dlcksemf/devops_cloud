from django.contrib import admin
from music.models import Music, Tag, Category


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

