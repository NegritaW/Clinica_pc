from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
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
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Las contraseñas no coinciden."))

        # Validar usando los validadores de Django (longitud, similitud, etc.)
        try:
            validate_password(password1, self.instance)
        except ValidationError as e:
            # Traducimos los mensajes de error al español
            mensajes_traducidos = []
            for msg in e.messages:
                if "too short" in msg:
                    mensajes_traducidos.append("La contraseña es demasiado corta (mínimo 8 caracteres).")
                elif "too common" in msg:
                    mensajes_traducidos.append("La contraseña es demasiado común, elige otra.")
                elif "too similar" in msg:
                    mensajes_traducidos.append("La contraseña es demasiado similar al nombre de usuario.")
                elif "entirely numeric" in msg:
                    mensajes_traducidos.append("La contraseña no puede ser solo números.")
                else:
                    mensajes_traducidos.append(msg)
            raise ValidationError(mensajes_traducidos)

        return password2


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
