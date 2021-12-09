from django.urls import path
from diary.views import post_list, post_detail, tag_detail

app_name = "diary"

urlpatterns = [
    path('', post_list, name="post_list"),
    path('<int:pk>/', post_detail, name="post_detail"),
    path('tags/<str:tag_name>/', tag_detail, name="tag_detail"),
]