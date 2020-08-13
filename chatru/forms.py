from django import forms
from .models import Translation


class TranslateForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ['texto']


