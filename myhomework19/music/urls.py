from django.urls import path
from music.views import music_list, music_detail, tag_detail

app_name = 'music'

urlpatterns = [
    path('', music_list, name="music_list"),
    path('<int:pk>/', music_detail, name="music_detail"),
    path('tags/<str:tag_name>', tag_detail, name="tag_detail"),
]