from .models import House
from django import forms

# This PostgreSQL Modal, which contains all the fields.


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
