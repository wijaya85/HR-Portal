
from dataclasses import field
from django.forms import ModelForm

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
       widget=forms.TextInput(
           attrs={
               'placeholder':'Masukkan Username',
               'class' : 'form-control'
           }
       )       
    )
        
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'**********',
                'class' : 'form-control'
            }
        )
    )    
    