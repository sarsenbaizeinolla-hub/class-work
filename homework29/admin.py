from django.contrib import admin
from .models import Booking, BookingObject


@admin.register(BookingObject)
class BookingObjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'car_type', 'capacity', 'price_per_hour')
  search_fields = ('name', 'description')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
  list_display = ('booking_object', 'user', 'date', 'start_time', 'end_time')
  list_filter = ('date', 'booking_object')