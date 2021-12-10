from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


def root(request):
    return redirect("shop:shop_new")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('', root, name="root"),
]
