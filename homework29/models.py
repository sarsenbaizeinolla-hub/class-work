from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BookingObject(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за час")
    image_url = models.URLField(verbose_name="Ссылка на фото", blank=True, null=True)
    is_available = models.BooleanField(default=True, verbose_name="Доступен")
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    booking_object = models.ForeignKey(BookingObject, on_delete=models.CASCADE, verbose_name="Объект")
    start_time = models.DateTimeField(default=timezone.now, verbose_name="Время начала")
    end_time = models.DateTimeField(default=timezone.now, verbose_name="Время конца")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    def __str__(self):
        return f"{self.user.username} - {self.booking_object.name}"