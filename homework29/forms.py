from django import forms
from .models import CarAd

class CarAdForm(forms.ModelForm):
    class Meta:
        model = CarAd
        fields = ['title', 'brand', 'price', 'description']