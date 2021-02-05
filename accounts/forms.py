from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

# User form will go here


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your last name'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email address'
                }
            )
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'date_birth', 'buyer_number',
                  'buyer_solicitor_name', 'household_income']
        widgets = {
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your address'
                }
            ),
            'date_birth': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the year born on...'
                }
            ),
            'buyer_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter buyers number'
                }
            ),
            'buyer_solicitor_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your solicitor name'
                }
            ),
            'household_income': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your household income'
                }
            ),
        }
