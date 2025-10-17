'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistrarUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nombre_completo', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
            'nombre_completo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo'
            }),
            # 👇 no agregamos los password aquí porque UserCreationForm ya los define
        }
        labels = {
            'username': 'Usuario',
            'nombre_completo': 'Nombre completo',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

    # 👇 agregamos los widgets personalizados para los campos de contraseña
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña'
        })
    )

    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña'
        })
    )


class AsignarRolForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rol', 'is_active']
        widgets = {
            'rol': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'rol': 'Rol del usuario',
            'is_active': 'Activo',
        }
'''