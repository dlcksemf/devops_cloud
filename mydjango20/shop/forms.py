from shop.models import Shop
from django import forms


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"
