from django.urls import path
from . import views
from .api_views import entrega_list_api

urlpatterns = [
    path('verificar/', views.verificar_equipo, name='verificar_equipo'),
    path('reporte/', views.reporte_entrega, name='reporte_entrega'),
    path('comprobante/<str:nombre>/', views.comprobante, name='comprobante'),
    #rutas api uwu
    path('', entrega_list_api, name="entrega_list_api"),
]