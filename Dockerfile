# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . .

# Собираем статику (если нужно)
RUN python manage.py collectstatic --noinput

# Запускаем приложение через gunicorn
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT