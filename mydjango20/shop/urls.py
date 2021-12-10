from django.urls import path
from shop.views import shop_new, shop_detail

app_name = "shop"

urlpatterns = [
    path("<int:pk>/", shop_detail, name="shop_detail"),
    path("new/", shop_new, name="shop_new"),
]