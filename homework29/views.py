from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    # Рендерит index.html из папки homework29/templates/homework29/
    return render(request, 'homework29/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('portfolio')
    else:
        form = UserCreationForm()
    # Рендерит register.html из папки homework29/templates/homework29/registration/
    return render(request, 'homework29/registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('portfolio')
    else:
        form = AuthenticationForm()
    # Рендерит login.html из папки homework29/templates/homework29/registration/
    return render(request, 'homework29/registration/login.html', {'form': form})
