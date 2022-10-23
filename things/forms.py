"""Forms of the project."""
from django import forms
from .models import Thing
from django.forms import ModelForm
from django.forms import Textarea
from django.forms import NumberInput



# Create your forms here.
class ThingForm(ModelForm):

    class Meta:
        model = Thing
        fields = ['name', 'description','quantity']

        widgets = {
            'description': Textarea(),
            'quantity': NumberInput(),
        }



