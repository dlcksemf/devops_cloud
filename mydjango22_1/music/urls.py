from django.urls import path
from music import views

app_name = "music"

urlpatterns = [
    path('',views.music_list, name="music_list"),

]