from django.urls import path

from music.views import music_index, music_detail, tag_detail


app_name = 'music'

urlpatterns = [
    path('', music_index, name='music_index'),
    path('<int:pk>/', music_detail, name='music_detail'),
    path('tags/<str:tag_name>', tag_detail, name='tag_detail')
]