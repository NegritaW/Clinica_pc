from django.urls import path
from . import views
from .api_views import EntregaListAPI, EntregaDetailAPI

urlpatterns = [
    path('verificar/', views.verificar_equipo, name='verificar_equipo'),
    path('reporte/', views.reporte_entrega, name='reporte_entrega'),
    path('comprobante/<str:nombre>/', views.comprobante, name='comprobante'),
    #rutas api uwu
    path('entregas/', EntregaListAPI.as_view(), name="api_entregas"),
    path('entregas/<int:pk>/', EntregaDetailAPI.as_view(), name="api_entrega_detalle"),
]