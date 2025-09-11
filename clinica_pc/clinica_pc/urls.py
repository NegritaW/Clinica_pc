"""
URL configuration for clinica_pc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views  # vistas del proyecto
from login import views as login_views  # 👈 importamos las del app login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # 👈 home en la raíz
    path('login/', login_views.login_view, name='login'),  # 👈 ESTA línea debe existir
    path('logout/', login_views.logout_view, name='logout'),
    path('protected/', login_views.protected_view, name='protected'),
]