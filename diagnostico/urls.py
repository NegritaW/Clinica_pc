from django.urls import path
from . import views
from .api_views import api_lista_diagnosticos, api_agregar_diagnostico, api_modificar_diagnostico

urlpatterns = [
    path('listado/', views.listado_diagnosticos, name="diagnostico_listado"),
    path('evaluar/', views.evaluar_equipo, name="diagnostico_evaluar"),
    path('eliminar/<str:nombre>/', views.eliminar_diagnostico, name="diagnostico_eliminar"),
    #rutas api uwu
    path('', api_lista_diagnosticos, name='api_lista_diagnosticos'),
    path('agregar/', api_agregar_diagnostico, name='api_agregar_diagnostico'),
    path('<int:pk>/modificar/', api_modificar_diagnostico, name='api_modificar_diagnostico'),
]