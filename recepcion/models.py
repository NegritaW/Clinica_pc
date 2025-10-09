from django.db import models

# Create your models here.
class Cliente(models.Model):
  nombre_cliente = models.CharField(max_length=100)
  tipo_equipo = models.CharField(max_length=100)
  problema_reportado = models.CharField(max_length=100)
  creado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nombre
  
  class Meta:
    ordering = ['-creado']

class Recepcion(models.Model):
  fecha_recepcion = models.DateTimeField(auto_now_add=True)
  recepcionista = models.CharField(max_length=150, blank=True)  # opcional: puede luego hacerse FK a RoleRecepcion
  observaciones = models.TextField(blank=True)

  def __str__(self):
      return f"Recepción {self.id} - {self.fecha_recepcion:%d-%m-%Y %H:%M}"