from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookingForm, RegistrationForm
from .models import Booking, SubscriptionType, Trainer, UserSubscription


def home_view(request):
  trainers = Trainer.objects.all()[:3]
  subscriptions = SubscriptionType.objects.all()[:3]
  return render(
      request,
      'fitness/home.html',
      {'trainers': trainers, 'subscriptions': subscriptions},
  )


def register_view(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(
          request, 'Регистрация прошла успешно! Теперь вы можете войти.'
      )
      return redirect('login')
  else:
    form = RegistrationForm()
  return render(request, 'fitness/register.html', {'form': form})


def trainers_view(request):
  trainers = Trainer.objects.all()
  return render(request, 'fitness/trainers.html', {'trainers': trainers})


def subscriptions_view(request):
  subscriptions = SubscriptionType.objects.all()
  return render(
      request, 'fitness/subscriptions.html', {'subscriptions': subscriptions}
  )


@login_required
def buy_subscription(request, sub_id):
  sub_type = get_object_or_404(SubscriptionType, id=sub_id)
  end_date = date.today() + timedelta(days=sub_type.duration_days)

  UserSubscription.objects.create(
      user=request.user, subscription_type=sub_type, end_date=end_date
  )
  messages.success(request, f'Вы успешно приобрели абонемент: {sub_type.name}!')
  return redirect('profile')


@login_required
def booking_view(request):
  if request.method == 'POST':
    form = BookingForm(request.POST)
    if form.is_valid():
      booking = form.save(commit=False)
      booking.user = request.user
      booking.save()
      messages.success(request, 'Тренировка успешно забронирована!')
      return redirect('profile')
  else:
    form = BookingForm()
  return render(request, 'fitness/booking.html', {'form': form})


@login_required
def profile_view(request):
  user_subscriptions = UserSubscription.objects.filter(user=request.user)
  user_bookings = Booking.objects.filter(user=request.user)
  return render(
      request,
      'fitness/profile.html',
      {'subscriptions': user_subscriptions, 'bookings': user_bookings},
  )