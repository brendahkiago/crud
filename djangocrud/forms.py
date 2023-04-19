from django import forms
from myapp.models import student


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['firstname', 'lastname', 'email']
