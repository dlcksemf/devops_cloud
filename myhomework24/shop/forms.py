from django import forms
from shop.models import Shop, Comment


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"