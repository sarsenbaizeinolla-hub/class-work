from django.apps import AppConfig


class Homework29Config(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'homework29'

  def ready(self):
    try:
      from .models import BookingObject

      if not BookingObject.objects.exists():
        cars = [
            {
                'name': 'Tesla Model S Plaid',
                'car_type': 'electric',
                'capacity': 5,
                'price_per_hour': 2500,
                'price_per_day': 18000,
                'description': (
                    'Флагманский электромобиль с невероятной динамикой разгона,'
                    ' автопилотом и футуристичным салоном.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'BMW M5 F90 Competition',
                'car_type': 'sport',
                'capacity': 5,
                'price_per_hour': 3000,
                'price_per_day': 22000,
                'description': (
                    'Мощный спортивный седан бизнес-класса: полный привод, престиж'
                    ' и взрывной характер.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'Mercedes-Benz G63 AMG',
                'car_type': 'suv',
                'capacity': 5,
                'price_per_hour': 4500,
                'price_per_day': 35000,
                'description': (
                    'Легендарный Гелик: рамный внедорожник с брутальным звуком'
                    ' выхлопа и премиальным комфортом.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1520031441872-265e4ff70366?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'Porsche 911 Carrera',
                'car_type': 'sport',
                'capacity': 2,
                'price_per_hour': 5000,
                'price_per_day': 40000,
                'description': (
                    'Культовый немецкий спорткар для незабываемых поездок и'
                    ' ярких эмоций.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'Toyota Camry XV70',
                'car_type': 'sedan',
                'capacity': 5,
                'price_per_hour': 1200,
                'price_per_day': 8500,
                'description': (
                    'Надежный и комфортный городской седан. Идеальный выбор на'
                    ' каждый день.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'Audi e-tron GT',
                'car_type': 'electric',
                'capacity': 4,
                'price_per_hour': 3500,
                'price_per_day': 26000,
                'description': (
                    'Элегантный электрический спорткар с футуристичным дизайном'
                    ' и безупречной управляемостью.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1614200187524-dc4b892acf16?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'Land Cruiser 300',
                'car_type': 'suv',
                'capacity': 7,
                'price_per_hour': 3200,
                'price_per_day': 24000,
                'description': (
                    'Флагманский внедорожник повышенной проходимости для всей'
                    ' семьи и дальних поездок.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1594834749899-6a8494ff6f2d?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'Kia K5 Style',
                'car_type': 'sedan',
                'capacity': 5,
                'price_per_hour': 1100,
                'price_per_day': 7900,
                'description': (
                    'Яркий молодежный седан с современными опциями и стильной'
                    ' светодиодной оптикой.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'Ford Mustang GT',
                'car_type': 'sport',
                'capacity': 4,
                'price_per_hour': 3800,
                'price_per_day': 28000,
                'description': (
                    'Американская классика с мотором V8, ревом выхлопа и'
                    ' невероятной харизмой.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1584345604476-8ec5e12e42dd?auto=format&fit=crop&w=800&q=80'
                ),
            },
            {
                'name': 'Hyundai Santa Fe',
                'car_type': 'suv',
                'capacity': 7,
                'price_per_hour': 1800,
                'price_per_day': 13000,
                'description': (
                    'Просторный семейный кроссовер с комфортным салоном и'
                    ' экономичным расходом.'
                ),
                'image_url': (
                    'https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=800&q=80'
                ),
            },
        ]
        for car in cars:
          BookingObject.objects.create(**car)
    except Exception:
      pass