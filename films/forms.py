from django import forms

from .models import Film
from .models import AIItem

class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ('titre', 'auteur', 'avis', 'dateVue')

class AiForm(forms.ModelForm):
    class Meta:
        model = AIItem
        fields = ["title", "description"]