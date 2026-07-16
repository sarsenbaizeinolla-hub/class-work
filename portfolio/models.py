from django.db import models
from django.contrib.auth.models import User

class CryptoAsset(models.Model):
    """
    Модель для хранения криптовалютных активов пользователя.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField(max_length=100, verbose_name="Название")
    symbol = models.CharField(max_length=10, verbose_name="Тикер")
    amount = models.DecimalField(max_digits=18, decimal_places=8, verbose_name="Количество")
    buy_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name="Цена покупки")

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.symbol} ({self.user.username})"