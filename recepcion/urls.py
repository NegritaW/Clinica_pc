from django.urls import path
from . import views
from .api_views import RecepcionListAPI, RecepcionDetailAPI

urlpatterns = [
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('listado/', views.listado_equipos, name='listado_equipos'),
    path('detalle/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
    #rutas api uwu
    path('recepciones/', RecepcionListAPI.as_view(), name="api_recepciones"),
    path('recepciones/<int:pk>/', RecepcionDetailAPI.as_view(), name="api_recepcion_detalle"),
]