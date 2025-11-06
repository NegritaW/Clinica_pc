from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.protected_view, name='protected'),
    path('loginregistro/', views.register_view, name='loginregistro'),
]