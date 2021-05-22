from django import forms
from .models import Companie, Vacancy, Responses

class PostForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'description', ]
