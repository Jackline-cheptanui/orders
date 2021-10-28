

from django import forms

from .models import Generateorder
class GenerateorderRegistrationForms(forms.ModelForm):
    class Meta:
        model=Generateorder
        fields="__all__"