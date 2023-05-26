from django import forms
from .models import Users

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ["date_registered"]


class CustomUserChangeForm(forms.ModelForm):
    pass