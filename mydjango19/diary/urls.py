from django.urls import path
from diary.views import post_list, post_detail, tag_detail, post_new, post_edit, comment_edit, comment_new

app_name = "diary"

urlpatterns = [
    path('', post_list, name="post_list"),
    path('<int:pk>/', post_detail, name="post_detail"),
    path("new/", post_new, name="post_new"),
    path("<int:pk>/edit/", post_edit, name="post_edit"),
    path('tags/<str:tag_name>/', tag_detail, name="tag_detail"),
    path("<int:post_pk>/comments/new/", comment_new, name="comment_new"),
    path("<int:post_pk>/comments/<int:pk>/edit/", comment_edit, name="comment_edit"),
]