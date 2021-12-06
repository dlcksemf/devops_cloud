
from django.urls import path
from melon.views import music_list, music_detail

app_name = 'melon'

urlpatterns = [
    path('', music_list, name="music_list"),
    path('<int:pk>/', music_detail, name="music_detail"),
]