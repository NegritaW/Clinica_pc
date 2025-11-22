from django.urls import path
from . import views
from .api_views import api_lista_entregas, api_agregar_entrega, api_modificar_entrega


urlpatterns = [
    path('verificar/', views.verificar_equipo, name='verificar_equipo'),
    path('reporte/', views.reporte_entrega, name='reporte_entrega'),
    path('comprobante/<str:nombre>/', views.comprobante, name='comprobante'),
    #rutas api uwu
    path('', api_lista_entregas, name='api_lista_entregas'),
    path('agregar/', api_agregar_entrega, name='api_agregar_entrega'),
    path('<int:pk>/modificar/', api_modificar_entrega, name='api_modificar_entrega'),
]