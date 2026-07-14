from django.contrib import admin
from .models import Parent, Child, Kiosk, IceCream

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Kiosk)
admin.site.register(IceCream)