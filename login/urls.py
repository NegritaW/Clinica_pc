from django.urls import path
from . import views
from .api_views import UsuarioListAPI, UsuarioDetailAPI

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.protected_view, name='protected'),
    path('loginregistro/', views.register_view, name='loginregistro'),
    #rutas api uwu
    path('usuarios/', UsuarioListAPI.as_view(), name="api_usuarios"),
    path('usuarios/<int:pk>/', UsuarioDetailAPI.as_view(), name="api_usuario_detalle"),
]