from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BookingObject, Booking
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def booking_list(request):
    """Список объектов и броней с пагинацией."""
    objects = BookingObject.objects.all()
    
    # Пагинация для броней
    all_bookings = Booking.objects.all()
    paginator = Paginator(all_bookings, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'homework29/booking_list.html', {
        'objects': objects,
        'page_obj': page_obj
    })