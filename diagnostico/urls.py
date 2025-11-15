from django.urls import path
from . import views
from .api_views import DiagnosticoListAPI, DiagnosticoDetailAPI

urlpatterns = [
    path('listado/', views.listado_diagnosticos, name="diagnostico_listado"),
    path('evaluar/', views.evaluar_equipo, name="diagnostico_evaluar"),
    path('eliminar/<str:nombre>/', views.eliminar_diagnostico, name="diagnostico_eliminar"),
    #rutas api uwu
    path('diagnosticos/', DiagnosticoListAPI.as_view(), name="api_diagnosticos"),
    path('diagnosticos/<int:pk>/', DiagnosticoDetailAPI.as_view(), name="api_diagnostico_detalle"),
]