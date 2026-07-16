import requests

def get_market_data():
    """Получает топ-10 монет с CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception:
        return []