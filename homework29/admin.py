from django.contrib import admin
from .models import BookingObject, Booking

@admin.register(BookingObject)
class BookingObjectAdmin(admin.ModelAdmin):
    # Исправили: было 'price_per_day', а в модели у нас 'price_per_hour'
    list_display = ('name', 'price_per_hour', 'is_available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Исправили: было 'start_date' и 'end_date', а в модели 'start_time' и 'end_time'
    list_display = ('user', 'booking_object', 'start_time', 'end_time')