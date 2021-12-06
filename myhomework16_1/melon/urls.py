
from django.urls import path
from melon.views import melon_list, melon_detail

app_name = 'melon'

urlpatterns = [
    path('', melon_list, name="music_list"),
    path('<int:pk>/', melon_detail, name="music_detail")
]