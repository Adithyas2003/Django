from django import forms
from .models import *

class normal_form(forms.Form):
    Name=forms.CharField()
    user_age=forms.IntegerField()
    email=forms.EmailField()
    place=forms.CharField()


class model_form(forms.ModelForm):
    class Meta:
        model=project_user
        fields='__all__'
        # fields=['name','age']
