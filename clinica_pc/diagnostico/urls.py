from django.urls import path
from . import views

urlpatterns = [
    path('listado/', views.listado_diagnosticos, name="diagnostico_listado"),
    path('evaluar/', views.evaluar_equipo, name="diagnostico_evaluar"),
    path('eliminar/<str:nombre>/', views.eliminar_diagnostico, name="diagnostico_eliminar"),
]