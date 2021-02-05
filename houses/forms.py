from .models import House
from django import forms


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
