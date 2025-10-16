from django.db import models
from login.models import Usuario

class Recepcion(models.Model):
  cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recepciones_cliente')
  recepcionista = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='recepciones_recepcionista')
  tipo_equipo = models.CharField(max_length=100)
  problema_reportado = models.TextField()
  observaciones = models.TextField(blank=True)
  fecha_recepcion = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Recepción {self.id} - {self.cliente.nombre_completo}"