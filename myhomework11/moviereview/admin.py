from django.contrib import admin
from moviereview.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "director", "rates", "watched_date"]
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
