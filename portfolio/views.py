from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CryptoAsset
from .forms import CryptoAssetForm

# Безопасный импорт, чтобы избежать ошибок, если модуль market отсутствует
try:
    from market.utils import get_market_data
except ImportError:
    def get_market_data(): return []

@login_required
def portfolio_view(request):
    # Обработка формы
    if request.method == 'POST':
        form = CryptoAssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.user = request.user
            asset.save()
            return redirect('portfolio')
    else:
        form = CryptoAssetForm()
    
    assets = CryptoAsset.objects.filter(user=request.user)
    
    # Получение рыночных данных
    try:
        market_data = get_market_data()
        prices = {coin['symbol'].upper(): coin['current_price'] for coin in market_data}
    except Exception:
        prices = {}
    
    # Расчет PnL
    for asset in assets:
        try:
            current_price = float(prices.get(asset.symbol.upper(), 0))
            asset.current_value = float(asset.amount) * current_price
            asset.pnl = asset.current_value - (float(asset.amount) * float(asset.buy_price))
        except (ValueError, TypeError):
            asset.current_value = 0
            asset.pnl = 0
    
    return render(request, 'portfolio/portfolio_list.html', {
        'assets': assets, 
        'form': form
    })

@login_required
def delete_asset(request, pk):
    asset = get_object_or_404(CryptoAsset, pk=pk, user=request.user)
    if request.method == 'POST':
        asset.delete()
        return redirect('portfolio')
    return render(request, 'portfolio/confirm_delete.html', {'asset': asset})