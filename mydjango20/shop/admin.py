from django.contrib import admin

from shop.forms import ShopForm
from shop.models import Shop, Review, Tag, Category


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form = ShopForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["shop"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
