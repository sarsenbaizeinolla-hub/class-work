from django.contrib.auth.models import User
from django.db import models


class BookingObject(models.Model):
  CAR_TYPES = [
      ('sedan', 'Седан'),
      ('suv', 'Внедорожник'),
      ('sport', 'Спортивный'),
      ('electric', 'Электромобиль'),
  ]

  name = models.CharField(
      max_length=100, verbose_name='Марка и модель авто'
  )
  car_type = models.CharField(
      max_length=20, choices=CAR_TYPES, default='sedan', verbose_name='Тип кузова'
  )
  capacity = models.IntegerField(default=5, verbose_name='Количество мест')
  price_per_hour = models.DecimalField(
      max_digits=8, decimal_places=2, verbose_name='Цена за час (₽)'
  )
  price_per_day = models.DecimalField(
      max_digits=8, decimal_places=2, verbose_name='Цена за день (₽)'
  )
  description = models.TextField(blank=True, verbose_name='Описание авто')
  image_url = models.URLField(
      max_length=500, blank=True, null=True, verbose_name='Ссылка на фото'
  )

  def __str__(self):
    return f'{self.name} ({self.get_car_type_display()})'


class Booking(models.Model):
  booking_object = models.ForeignKey(
      BookingObject, on_delete=models.CASCADE, verbose_name='Автомобиль'
  )
  user = models.ForeignKey(
      User, on_delete=models.CASCADE, verbose_name='Клиент'
  )
  date = models.DateField(verbose_name='Дата аренды')
  start_time = models.TimeField(verbose_name='Время начала')
  end_time = models.TimeField(verbose_name='Время окончания')
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name='Дата создания'
  )

  def __str__(self):
    return f'{self.booking_object.name} — {self.user.username} ({self.date})'