from django import forms
from .models import Companie, Vacancy, Responses

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companie
        fields = ['name', 'description', 'site', 'logo']
