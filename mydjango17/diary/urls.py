from django.urls import path
from diary.views import post_list

app_name = "diary"

urlpatterns = [
    path('', post_list, name="post_list"),
]