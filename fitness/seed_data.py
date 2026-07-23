import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from homework29.models import BookingObject

objects = [
    {
        "name": "Премиум Офис",
        "description": "Идеальное место для деловых встреч в центре города.",
        "price_per_hour": 20.00,
        "image_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Студия звукозаписи",
        "description": "Профессиональная аппаратура для записи подкастов и музыки.",
        "price_per_hour": 35.50,
        "image_url": "https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Творческий Лофт",
        "description": "Просторное помещение для мастер-классов и креативных сессий.",
        "price_per_hour": 25.00,
        "image_url": "https://images.unsplash.com/photo-1517502884422-41eaead166d4?auto=format&fit=crop&w=800&q=80"
    }
]

for obj in objects:
    BookingObject.objects.get_or_create(**obj)
print("Каталог с картинками успешно создан!")