from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path('', views.shop_list, name="shop_list"),
    path('<int:pk>/', views.shop_detail, name="shop_detail"),
    path('new/', views.shop_new, name="shop_new"),
    path('<int:pk>/edit/', views.shop_edit, name="shop_edit"),
    path('<int:pk>/delete/', views.shop_delete, name="shop_delete"),
    path('<int:pk>/comment/new/', views.comment_new, name="comment_new"),
    path('<int:post_pk>/comment/<int:pk>/edit/', views.comment_edit, name="comment_edit"),
    path('<int:post_pk>/comment/<int:pk>/delete/', views.comment_delete, name="comment_delete"),
]