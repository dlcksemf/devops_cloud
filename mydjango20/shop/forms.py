from shop.models import Shop, Review
from django import forms


class ShopForm(forms.ModelForm):
    tags = forms.CharField()

    class Meta:
        model = Shop
        fields = [
            "category",
            "name",
            "telephone",
            "description",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "author_name",
            "message",
        ]