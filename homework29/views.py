from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Booking, BookingObject


def index(request):
  cars = BookingObject.objects.all()

  search_query = request.GET.get('q')
  car_type = request.GET.get('type')
  max_price = request.GET.get('max_price')
  min_capacity = request.GET.get('min_capacity')

  if search_query:
    cars = cars.filter(name__icontains=search_query) | cars.filter(
        description__icontains=search_query
    )
  if car_type and car_type != 'any':
    cars = cars.filter(car_type=car_type)
  if max_price:
    try:
      cars = cars.filter(price_per_hour__lte=float(max_price))
    except ValueError:
      pass
  if min_capacity:
    try:
      cars = cars.filter(capacity__gte=int(min_capacity))
    except ValueError:
      pass

  return render(request, 'homework29/index.html', {'cars': cars})


def room_detail(request, pk):
  car = get_object_or_404(BookingObject, pk=pk)
  all_cars = BookingObject.objects.all()

  date_str = request.GET.get('date')
  if not date_str:
    date_str = datetime.today().strftime('%Y-%m-%d')

  try:
    selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
  except (ValueError, TypeError):
    selected_date = datetime.today().date()

  if request.method == 'POST' and request.user.is_authenticated:
    start_time_str = request.POST.get('start_time')
    if start_time_str:
      start_time = datetime.strptime(start_time_str, '%H:%M').time()
      dt_obj = datetime.combine(selected_date, start_time) + timedelta(hours=1)
      end_time = dt_obj.time()

      exists = Booking.objects.filter(
          booking_object=car, date=selected_date, start_time=start_time
      ).exists()

      if not exists:
        Booking.objects.create(
            booking_object=car,
            user=request.user,
            date=selected_date,
            start_time=start_time,
            end_time=end_time,
        )
        return redirect('booking_list')

  hours_slots = [
      ('08:00', '09:00'),
      ('09:00', '10:00'),
      ('10:00', '11:00'),
      ('11:00', '12:00'),
      ('12:00', '13:00'),
      ('13:00', '14:00'),
      ('14:00', '15:00'),
      ('15:00', '16:00'),
      ('16:00', '17:00'),
      ('17:00', '18:00'),
      ('18:00', '19:00'),
      ('19:00', '20:00'),
      ('20:00', '21:00'),
      ('21:00', '22:00'),
  ]

  booked_slots = Booking.objects.filter(booking_object=car, date=selected_date)
  booked_times = [b.start_time.strftime('%H:%M') for b in booked_slots]

  context = {
      'room': car,
      'all_rooms': all_cars,
      'selected_date': selected_date,
      'hours_slots': hours_slots,
      'booked_times': booked_times,
  }
  return render(request, 'homework29/room_detail.html', context)


@login_required
def booking_list(request):
  bookings = Booking.objects.filter(user=request.user).order_by(
      '-date', '-start_time'
  )
  return render(request, 'homework29/booking_list.html', {'bookings': bookings})


def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
  else:
    form = UserCreationForm()
  return render(request, 'homework29/register.html', {'form': form})


def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('index')
  else:
    form = AuthenticationForm()
  return render(request, 'homework29/login.html', {'form': form})


def logout_view(request):
  logout(request)
  return redirect('index')