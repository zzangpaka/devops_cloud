from django import forms
from shop.models import Shop, Resell


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'


class ResellForm(forms.ModelForm):
    class Meta:
        model = Resell
        fields = '__all__'