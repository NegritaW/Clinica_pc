from django.db import models
from login.models import Usuario
from recepcion.models import Recepcion

class Entrega(models.Model):
    recepcion = models.ForeignKey(Recepcion, on_delete=models.CASCADE, related_name='entregas')
    entregado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='entregas_entregadas')
    observaciones = models.TextField(blank=True)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="entregado")

    def __str__(self):
        return f"Entrega {self.id} - {self.recepcion.cliente.nombre_completo}"
