from django.contrib import admin
from .models import BookingObject, Booking

@admin.register(BookingObject)
class BookingObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_day')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_object', 'start_date', 'end_date')