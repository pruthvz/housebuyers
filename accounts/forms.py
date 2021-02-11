from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

# User form will go here

# This class contains all the fields the built in register page provides you. These fields are built within Django


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User  # calling the User built in modal that works with login/register
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']  # the fields that are inside that modal
        # What I'm doing here is, styling the fields since you can't really alter python fields in Html.
        # adding simple stylign and placeholders to these fields.
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

# This class contains all the feilds that wasn't built within the User function.


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'date_birth', 'buyer_number',
                  'buyer_solicitor_name', 'household_income']  # extra feilds
        # styling the fields again, which will be displayed within the register.html
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
