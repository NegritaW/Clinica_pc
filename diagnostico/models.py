from django.db import models
from login.models import Usuario
from recepcion.models import Recepcion

class Diagnostico(models.Model):
    ESTADO_CHOICES = [
        ('asignado', 'Asignado'),
        ('en_progreso', 'En progreso'),
        ('finalizado', 'Finalizado'),
    ]

    recepcion = models.ForeignKey(Recepcion, on_delete=models.CASCADE, related_name='diagnosticos')
    tecnico = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='diagnosticos_tecnico')
    diagnostico_text = models.TextField(blank=True)
    solucion_text = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='asignado')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Diagnóstico #{self.id} - {self.recepcion.cliente.nombre_completo}"