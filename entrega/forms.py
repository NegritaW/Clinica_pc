'''
from django import forms
from .models import Entrega

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['recepcion', 'entregado_por', 'observaciones']
        widgets = {
            'recepcion': forms.Select(attrs={'class': 'form-select'}),
            'entregado_por': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones de entrega'}),
        }
'''