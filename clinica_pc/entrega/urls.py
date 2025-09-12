from django.urls import path
from . import views

urlpatterns = [
    path('verificar/', views.verificar_equipo, name='verificar_equipo'),
    path('reporte/', views.reporte_entrega, name='reporte_entrega'),
    path('comprobante/<str:nombre>/', views.comprobante, name='comprobante'),
]