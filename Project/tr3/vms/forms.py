from django import forms
from .models import Employee, Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
