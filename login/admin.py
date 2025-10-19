from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)  # Registra el modelo y usa la configuración de UserAdmin
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'nombre_completo', 'rol', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('rol', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'nombre_completo', 'rol')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('nombre_completo', 'rol')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

