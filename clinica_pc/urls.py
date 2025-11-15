from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('login.urls')),        # 👈 login separado y funcional
    path('recepcion/', include('recepcion.urls')),
    path('diagnostico/', include('diagnostico.urls')),           
    path('entrega/', include('entrega.urls')),
    #rutas api uwu
    path("api/login/", include("login.urls")),
    path("api/recepcion/", include("recepcion.urls")),
    path("api/diagnostico/", include("diagnostico.urls")),
    path("api/entrega/", include("entrega.urls")),
]