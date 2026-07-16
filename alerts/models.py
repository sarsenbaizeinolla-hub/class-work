from django.db import models
from django.contrib.auth.models import User

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    symbol = models.CharField(max_length=10, verbose_name="Тикер монеты")
    target_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name="Целевая цена")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    # Добавляем поле для связи с Telegram
    telegram_chat_id = models.CharField(max_length=50, verbose_name="Telegram Chat ID", default="0")

    def __str__(self):
        return f"{self.user.username} - {self.symbol} при {self.target_price}"
