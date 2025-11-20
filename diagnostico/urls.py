from django.urls import path
from . import views
from .api_views import diagnostico_list_api

urlpatterns = [
    path('listado/', views.listado_diagnosticos, name="diagnostico_listado"),
    path('evaluar/', views.evaluar_equipo, name="diagnostico_evaluar"),
    path('eliminar/<str:nombre>/', views.eliminar_diagnostico, name="diagnostico_eliminar"),
    #rutas api uwu
    path('', diagnostico_list_api, name="diagnostico_list_api"),
]