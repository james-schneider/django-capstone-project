from django import forms
from django.forms import fields, CheckboxInput
from .models import Note
from django.forms.models import inlineformset_factory

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('text', 'author')