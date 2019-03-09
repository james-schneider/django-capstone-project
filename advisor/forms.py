from django import forms
from .models import Advisee

class Notes(forms.ModelForm):
    class Meta:
        model=Advisee
        fields=['notes']