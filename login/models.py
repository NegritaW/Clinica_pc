from django.contrib.auth.models import AbstractUser, Group, Permission
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

    groups = models.ManyToManyField(
        Group,
        related_name='login_usuarios',  # Cambia esto para evitar conflicto
        blank=True,
        help_text='Los grupos a los que pertenece el usuario.',
        verbose_name='grupos',
        related_query_name='login_usuario',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='login_usuarios_permisos',  # Cambia esto para evitar conflicto
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos de usuario',
        related_query_name='login_usuario_permiso',
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_rol_display() if self.rol else 'Sin rol'})"


