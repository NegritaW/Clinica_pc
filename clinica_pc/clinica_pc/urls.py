from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('login.urls')),
    path('recepcion/', include('recepcion.urls')),
    path('diagnostico/', include('diagnostico.urls')),           
    path('entrega/', include('entrega.urls'))
]