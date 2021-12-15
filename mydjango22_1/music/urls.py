from django.urls import path
from music import views

app_name = "music"

urlpatterns = [
    path('',views.music_list, name="music_list"),
    path('new/', views.music_new, name="music_new"),
    path('<int:pk>/', views.music_detail, name="music_detail"),
    path('<int:pk>/edit/', views.music_edit, name="music_edit"),
]