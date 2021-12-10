from django.urls import path
from shop.views import shop_new, shop_detail, shop_edit, shop_list, review_new, review_edit, tag_detail

app_name = "shop"

urlpatterns = [
    path("", shop_list, name="shop_list"),
    path("<int:pk>/", shop_detail, name="shop_detail"),
    path("new/", shop_new, name="shop_new"),
    path("edit/<int:shop_pk>/", shop_edit, name="shop_edit"),
    path("<int:shop_pk>/review/new/", review_new, name="review_new"),
    path("<int:shop_pk>/review/<int:pk>/edit/", review_edit, name="review_edit"),
    path("tag/<str:tag_name>", tag_detail, name="tag_detail")
]