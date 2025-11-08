from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('listado/', views.listado_equipos, name='listado_equipos'),
    path('detalle/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
]