from django.db import models
from django.contrib.auth.models import User

class BookingObject(models.Model):
    """Объект для бронирования."""
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за день")
    image = models.ImageField(upload_to='objects/', verbose_name="Фото", blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    """Запись бронирования."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    booking_object = models.ForeignKey(BookingObject, on_delete=models.CASCADE, verbose_name="Объект")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
