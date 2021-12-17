from django import forms
from shop.models import Shop, Review


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            "category",
            "name",
            "description",
            "photo",
            "tag_set",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["message",]