from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'



class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }