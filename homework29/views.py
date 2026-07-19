from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import BookingObject, Booking

def index(request):
    """Главная страница: вывод всех объектов."""
    # Создаем тестовые данные при первом запуске
    if not BookingObject.objects.exists():
        BookingObject.objects.create(
            name="Премиум Офис", 
            description="Идеальное место для деловых встреч в центре города.", 
            price_per_hour=20.00,
            image_url="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80"
        )
        BookingObject.objects.create(
            name="Студия звукозаписи", 
            description="Профессиональная аппаратура для записи подкастов и музыки.", 
            price_per_hour=35.50,
            image_url="https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=800&q=80"
        )
    
    objects = BookingObject.objects.all()
    return render(request, 'homework29/ad_list.html', {'objects': objects})

@login_required
def booking_list(request):
    """Страница бронирования."""
    if request.method == 'POST':
        obj_id = request.POST.get('object_id')
        start = request.POST.get('start')
        end = request.POST.get('end')
        
        try:
            obj = BookingObject.objects.get(id=obj_id)
            Booking.objects.create(
                user=request.user,
                booking_object=obj,
                start_time=start,
                end_time=end
            )
        except Exception as e:
            print(f"Ошибка бронирования: {e}")
        return redirect('booking_list')

    objects = BookingObject.objects.all()
    return render(request, 'homework29/booking_list.html', {'objects': objects})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'homework29/registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'homework29/registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')