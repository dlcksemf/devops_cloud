from django.contrib import admin
from orange.models import Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ["title", "album_cover_file"]

admin.site.register(Music, MusicAdmin)
