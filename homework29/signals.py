from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model # Импортируем функцию для получения текущей модели

# Получаем активную модель пользователя
User = get_user_model()

@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Новый пользователь создан: {instance.username}")
def create_student_profile(sender, instance, created, **kwargs):
    """Автоматически создает профиль при создании нового пользователя"""
    if created:
        StudentProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    """Автоматически сохраняет профиль при изменении пользователя"""
    # Проверяем на всякий случай, есть ли у пользователя профиль, прежде чем сохранять
    if hasattr(instance, 'profile'):
        instance.profile.save()