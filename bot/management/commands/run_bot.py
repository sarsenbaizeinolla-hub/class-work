import os
import django
# STREAMING_CHUNK:Настройка окружения Django для работы бота
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management.base import BaseCommand
import telebot
from portfolio.models import CryptoAsset

# ВАШ ТОКЕН
BOT_TOKEN = "8800963118:AAGL-YXuIdX2RYpYIHN253oEJ7zA7_Eywzg"
bot = telebot.TeleBot(BOT_TOKEN)

# STREAMING_CHUNK:Определение команд бота
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот вашего Крипто-Трекера. Напиши /portfolio, чтобы увидеть свои активы.")

@bot.message_handler(commands=['portfolio'])
def show_portfolio(message):
    # Получаем все активы из базы данных
    assets = CryptoAsset.objects.all()
    if not assets:
        bot.reply_to(message, "Ваш портфель пока пуст.")
        return
    
    response = "📊 Ваш крипто-портфель:\n\n"
    for asset in assets:
        response += f"🔹 {asset.name} ({asset.symbol}): {asset.amount}\n"
    bot.reply_to(message, response)

# STREAMING_CHUNK:Создание команды для manage.py
class Command(BaseCommand):
    help = 'Запуск Telegram бота'

    def handle(self, *args, **kwargs):
        self.stdout.write("Бот запущен...")
        bot.infinity_polling()