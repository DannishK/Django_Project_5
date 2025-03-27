
from django import forms

from hosi.models import Appointment, Query, Newsletter, DoctorID
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your name'}),
            'number': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Enter your number'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your email'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your description'}),
            'visit_date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Enter your date'}),
        }

class QueryForm(forms.ModelForm):
    class Meta:
      model = Query
      fields = '__all__'
      widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your name'}),
        'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your email'}),
        'subject': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your subject'}),
        'message': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your message'}),



    }

class NewsletterForm(forms.ModelForm):
    class Meta:
      model = Newsletter
      fields = '__all__'
      widgets = {
        'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your email'}),
    }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DoctorIDForm(forms.ModelForm):
    class Meta:
        model = DoctorID
        fields =['doctor_identifier']


