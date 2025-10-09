from django.db import models

class Entrega(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    tipo_equipo = models.CharField(max_length=100)
    problema_reportado = models.TextField()
    tecnico_asignado = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, default="entregado")
    observaciones = models.TextField(blank=True)
    fecha_entrega = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrega de {self.nombre_cliente} ({self.estado})"
