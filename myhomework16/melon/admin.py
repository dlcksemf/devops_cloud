from django.contrib import admin
from melon.models import Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["title"]



