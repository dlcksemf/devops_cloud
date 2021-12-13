from django.urls import path
from shop.views import shop_new, shop_edit, shop_list, shop_detail


app_name = "shop"

urlpatterns = [
    path('', shop_list, name="shop_list"),
    path('<int:pk>/', shop_detail, name="shop_detail"),
    path('new/', shop_new, name="shop_new"),
    path('<int:shop_pk>/edit/', shop_edit, name="shop_edit"),
]