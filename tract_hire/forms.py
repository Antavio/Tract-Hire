from django import forms
from .models import *

class TractorForm(forms.ModelForm):
    class Meta:
        model = Tractor
        exclude = ['user']