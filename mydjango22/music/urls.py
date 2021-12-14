from django.urls import path
from music.views import music_list, music_detail, music_new, music_edit

app_name = "music"

urlpatterns = [
    path('', music_list, name="music_list"),
    path('<int:pk>', music_detail, name="music_detail"),
    path('new/', music_new, name="music_new"),
    path('<int:pk>/edit/', music_edit, name="music_edit"),
]