from django.urls import path
from diary.views import post_list, post_detail, tag_detail, post_new

app_name = "diary"

urlpatterns = [
    path('', post_list, name="post_list"),
    path('<int:pk>/', post_detail, name="post_detail"),
    path("new/", post_new, name="post_new"),
    path('tags/<str:tag_name>/', tag_detail, name="tag_detail"),
]