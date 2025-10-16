from django import forms
from .models import Recepcion

class RecepcionForm(forms.ModelForm):
  class Meta:
    model = Recepcion
    fields = ['cliente', 'recepcionista', 'tipo_equipo', 'problema_reportado', 'observaciones']
    widgets = {
      'cliente': forms.Select(attrs={'class': 'form-select'}),
      'recepcionista': forms.Select(attrs={'class': 'form-select'}),
      'tipo_equipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Notebook, PC, etc.'}),
      'problema_reportado': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describa el problema'}),
      'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
    }
