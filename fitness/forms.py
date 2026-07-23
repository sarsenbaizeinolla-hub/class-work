from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking


class RegistrationForm(UserCreationForm):
  email = forms.EmailField(
      required=True, widget=forms.EmailInput(attrs={'class': 'form-control'})
  )

  class Meta:
    model = User
    fields = ['username', 'email']
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'


class BookingForm(forms.ModelForm):

  class Meta:
    model = Booking
    fields = ['trainer', 'date', 'time']
    widgets = {
        'trainer': forms.Select(attrs={'class': 'form-select'}),
        'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    }