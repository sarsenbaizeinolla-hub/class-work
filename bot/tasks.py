import requests
from alerts.models import Alert
# Импорт вашей функции получения цен
from market.utils import get_market_data 

def check_alerts_and_notify(bot_token):
    market_data = get_market_data()
    prices = {coin['symbol'].upper(): coin['current_price'] for coin in market_data}
    
    active_alerts = Alert.objects.filter(is_active=True)
    
    for alert in active_alerts:
        current_price = prices.get(alert.symbol.upper(), 0)
        if current_price >= float(alert.target_price):
            # Отправка сообщения в Telegram
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {
                "chat_id": alert.telegram_chat_id,
                "text": f"🚀 Внимание! {alert.symbol} достиг цены ${current_price}"
            }
            requests.post(url, data=payload)
            
            # Отключаем алерт, чтобы не спамить
            alert.is_active = False
            alert.save()