from django.urls import path
from . import views
from .api_views import usuario_list_api

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.protected_view, name='protected'),
    path('loginregistro/', views.register_view, name='loginregistro'),
    #rutas api uwu
    path('api/usuarios/', usuario_list_api, name="usuario_list_api")
]