from django import forms
from .models import CryptoAsset

class CryptoAssetForm(forms.ModelForm):
    class Meta:
        model = CryptoAsset
        fields = ['name', 'symbol', 'amount', 'buy_price']
        labels = {
            'name': 'Название монеты',
            'symbol': 'Тикер (напр. BTC)',
            'amount': 'Количество',
            'buy_price': 'Цена покупки ($)',
        }