import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from homework29.models import BookingObject

# Очищаем старые объекты, чтобы не было дубликатов
BookingObject.objects.all().delete()

cars_data = [
    {
        'name': 'Tesla Model S Plaid',
        'car_type': 'electric',
        'capacity': 5,
        'price_per_hour': 35.00,
        'description': (
            'Флагманский электромобиль с невероятной динамикой разгона и'
            ' передовым автопилотом.'
        ),
        'image_url': 'https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=800&q=80',
    },
    {
        'name': 'BMW M5 Competition',
        'car_type': 'sport',
        'capacity': 5,
        'price_per_hour': 45.00,
        'description': (
            'Спортивный бизнес-седан сочетающий комфорт премиум-класса и трековую'
            ' мощь.'
        ),
        'image_url': 'https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=800&q=80',
    },
    {
        'name': 'Mercedes-Benz G63 AMG',
        'car_type': 'suv',
        'capacity': 5,
        'price_per_hour': 60.00,
        'description': (
            'Легендарный внедорожник с узнаваемым брутальным дизайном и роскошным'
            ' салоном.'
        ),
        'image_url': 'https://images.unsplash.com/photo-1520031441872-265e4ff70366?auto=format&fit=crop&w=800&q=80',
    },
    {
        'name': 'Porsche 911 Carrera',
        'car_type': 'sport',
        'capacity': 2,
        'price_per_hour': 75.00,
        'description': (
            'Культовый спортивный автомобиль для ярких эмоций и незабываемых'
            ' поездок.'
        ),
        'image_url': 'https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=800&q=80',
    },
    {
        'name': 'Toyota Camry XV70',
        'car_type': 'sedan',
        'capacity': 5,
        'price_per_hour': 15.00,
        'description': (
            'Комфортный и надежный городской седан для повседневных поездок.'
        ),
        'image_url': 'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?auto=format&fit=crop&w=800&q=80',
    },
    {
        'name': 'Audi e-tron GT',
        'car_type': 'electric',
        'capacity': 4,
        'price_per_hour': 50.00,
        'description': (
            'Элегантный электрический гран-туризмо с футуристичным дизайном.'
        ),
        'image_url': 'https://images.unsplash.com/photo-1614200187524-dc4b892acf16?auto=format&fit=crop&w=800&q=80',
    },
]

for car in cars_data:
  BookingObject.objects.create(**car)
  print(f"Добавлено авто: {car['name']}")

print('Все тестовые машины успешно загружены!')