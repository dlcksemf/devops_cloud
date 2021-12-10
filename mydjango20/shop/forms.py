from shop.models import Shop, Review
from django import forms


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "author_name",
            "message",
        ]