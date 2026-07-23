from django.conf import settings
from django.db import models


class Trainer(models.Model):
  name = models.CharField(max_length=100, verbose_name='Имя тренера')
  specialization = models.CharField(max_length=100, verbose_name='Специализация')
  bio = models.TextField(verbose_name='О тренере')
  experience_years = models.PositiveIntegerField(verbose_name='Опыт (лет)')
  image = models.ImageField(
      upload_to='trainers/', blank=True, null=True, verbose_name='Фото'
  )

  def __str__(self):
    return self.name


class SubscriptionType(models.Model):
  name = models.CharField(max_length=100, verbose_name='Название абонемента')
  description = models.TextField(verbose_name='Описание')
  price = models.DecimalField(
      max_digits=10, decimal_places=2, verbose_name='Цена (тенге)'
  )
  duration_days = models.PositiveIntegerField(
      verbose_name='Срок действия (дней)'
  )
  image = models.ImageField(
      upload_to='subscriptions/', blank=True, null=True, verbose_name='Картинка'
  )

  def __str__(self):
    return self.name


class UserSubscription(models.Model):
  user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      verbose_name='Пользователь',
  )
  subscription_type = models.ForeignKey(
      SubscriptionType, on_delete=models.CASCADE, verbose_name='Абонемент'
  )
  purchase_date = models.DateField(
      auto_now_add=True, verbose_name='Дата покупки'
  )
  end_date = models.DateField(verbose_name='Дата окончания')

  def __str__(self):
    return f'{self.user.username} - {self.subscription_type.name}'


class Booking(models.Model):
  user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      verbose_name='Пользователь',
  )
  trainer = models.ForeignKey(
      Trainer, on_delete=models.CASCADE, verbose_name='Тренер'
  )
  date = models.DateField(verbose_name='Дата тренировки')
  time = models.TimeField(verbose_name='Время тренировки')
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name='Дата создания'
  )

  def __str__(self):
    return (
        f'{self.user.username} -> {self.trainer.name} ({self.date} в'
        f' {self.time})'
    )