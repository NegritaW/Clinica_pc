from django.urls import path
from . import views
from .api_views import recepcion_list_api

urlpatterns = [
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('listado/', views.listado_equipos, name='listado_equipos'),
    path('detalle/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
    #rutas api uwu
    path('', recepcion_list_api, name="recepcion_list_api"),
]