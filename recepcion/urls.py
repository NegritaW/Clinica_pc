from django.urls import path
from . import views
from .api_views import api_lista_recepciones, api_agregar_recepcion, api_modificar_recepcion

urlpatterns = [
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('listado/', views.listado_equipos, name='listado_equipos'),
    path('detalle/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
    #rutas api uwu
    path('', api_lista_recepciones, name='api_lista_recepciones'),
    path('agregar/', api_agregar_recepcion, name='api_agregar_recepcion'),
    path('<int:pk>/modificar/', api_modificar_recepcion, name='api_modificar_recepcion'),
]