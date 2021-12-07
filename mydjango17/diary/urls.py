from django.urls import path
from diary.views import post_list, post_detail

app_name = "diary"

urlpatterns = [
    path('', post_list, name="post_list"),
    path('<int:pk>/', post_detail, name="post_detail"),
]