from django import forms
from django.forms import fields, CheckboxInput

from django import forms

from .models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('text', 'author')