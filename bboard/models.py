from django.db import models

class Task(models.Model):
    """Модель задачи для хранения данных о делах."""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")

    def __str__(self):
        return self.title