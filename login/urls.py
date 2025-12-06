from django.urls import path
from . import views
from .api_views import api_lista_usuarios, api_agregar_usuario, api_modificar_usuario, api_eliminar_usuario

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.protected_view, name='protected'),
    path('loginregistro/', views.register_view, name='loginregistro'),
    #rutas api uwu
    path('api/usuarios/', api_lista_usuarios, name='api_lista_usuarios'),
    path('api/usuarios/agregar/', api_agregar_usuario, name='api_agregar_usuario'),
    path('api/usuarios/<int:pk>/modificar/', api_modificar_usuario, name='api_modificar_usuario'),
    path('api/usuarios/eliminar/<int:pk>/', api_eliminar_usuario, name='api_eliminar_usuario'),
]