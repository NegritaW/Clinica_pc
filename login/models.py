from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ("admin", "Administrador"),
        ("tecnico", "Técnico / Diagnóstico"),
        ("recepcion", "Recepción / Entrega"),
    ]

    nombre_completo = models.CharField(max_length=150)
    rol = models.CharField(max_length=20, choices=ROLES, null=True, blank=True)
    is_active = models.BooleanField(default=False)  # El admin lo activa después del registro

    def __str__(self):
        return f"{self.username} ({self.get_rol_display() if self.rol else 'Sin rol'})"


