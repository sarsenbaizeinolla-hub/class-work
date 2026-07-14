from django.db import models

# СВЯЗЬ: РОДИТЕЛЬ И РЕБЕНОК
class Parent(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя родителя")
    age = models.IntegerField(verbose_name="Возраст")

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя ребенка")
    age = models.IntegerField(verbose_name="Возраст")
    # ForeignKey — это связь "многие к одному" (у одного родителя много детей)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children', verbose_name="Родитель")

    def __str__(self):
        return self.name

# СВЯЗЬ: КИОСК И МОРОЖЕНОЕ
class Kiosk(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адрес киоска")

    def __str__(self):
        return self.address

class IceCream(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название мороженого")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    # Связь: в одном киоске может быть много видов мороженого
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE, related_name='ice_creams', verbose_name="Киоск")

    def __str__(self):
        return self.name