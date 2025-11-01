from django import forms
from .models import Destination, Country

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class DestinationForm(forms.ModelForm):
    class Meta:
        model=Destination
        fields=['name','country','description','average_cost','rating','image','video']