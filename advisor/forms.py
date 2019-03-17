from django import forms
from .models import Advisee, Note

class NoteForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['text', 'advisee']
