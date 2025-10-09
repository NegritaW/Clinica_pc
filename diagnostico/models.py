from django.db import models

# Create your models here.
class Diagnostico(models.Model):
  ESTADO_CHOICES = [
        ('asignado', 'Asignado'),
        ('en_progreso', 'En progreso'),
        ('finalizado', 'Finalizado'),
  ]

  equipo = models.CharField(max_length=100)
  diagnostico_text = models.TextField(blank=True)
  solucion_text = models.TextField(blank=True)
  estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='asignado')
  creado = models.DateTimeField(auto_now_add=True)
  actualizado = models.DateTimeField(auto_now=True)