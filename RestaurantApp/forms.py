from django import forms
from . import models

class ReserveForm(forms.ModelForm):
    class Meta:
        model=models.ReserveTable
        fields="__all__"




 