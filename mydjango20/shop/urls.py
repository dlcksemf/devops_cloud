from django.urls import path
from shop.views import shop_new, shop_detail, shop_edit

app_name = "shop"

urlpatterns = [
    path("<int:pk>/", shop_detail, name="shop_detail"),
    path("new/", shop_new, name="shop_new"),
    path("edit/<int:shop_pk>/", shop_edit, name="shop_edit")
]