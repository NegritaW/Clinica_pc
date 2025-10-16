from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistrarUsuario(UserCreationForm):
  class Meta:
    model = Usuario
    fields = ['username', 'nombre_completo', 'password1', 'password2']
    widgets = {
      'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
      'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}),
    }
    labels = {
      'username': 'Usuario',
      'nombre_completo': 'Nombre completo',
    }
  
class AsignarRolForm(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = ['rol', 'is_active']
    widgets = {
      'rol': forms.Select(attrs={'class': 'form-select'}),
      'is_active': forms.CheckboxInput(),
    }