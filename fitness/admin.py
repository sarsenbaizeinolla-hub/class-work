from django.contrib import admin
from .models import Booking, SubscriptionType, Trainer, UserSubscription

admin.site.register(Trainer)
admin.site.register(SubscriptionType)
admin.site.register(UserSubscription)
admin.site.register(Booking)