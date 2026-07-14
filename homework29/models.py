from django.db import models
from django.contrib.auth.models import User

class CarAd(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название авто")
    brand = models.CharField(max_length=50, verbose_name="Марка")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")

    def __str__(self):
        return self.title