from django import forms
from .models import Diagnostico

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['recepcion', 'tecnico', 'diagnostico_text', 'solucion_text', 'estado']
        widgets = {
            'recepcion': forms.Select(attrs={'class': 'form-select'}),
            'tecnico': forms.Select(attrs={'class': 'form-select'}),
            'diagnostico_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese diagnóstico técnico'}),
            'solucion_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la solución aplicada'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }