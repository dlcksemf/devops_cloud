from django.contrib import admin
from orange.models import Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ["title", "album_cover"]


admin.site.register(Music, MusicAdmin)

# admin.site.register(Music)