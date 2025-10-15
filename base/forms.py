from django.forms import ModelForm as m
from .models import Destination

class DestinationForm(m):
    class Meta:
        model=Destination
        fields=['name','country','description','average_cost','rating']