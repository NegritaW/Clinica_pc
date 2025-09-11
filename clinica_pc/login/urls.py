from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.protected_view, name='protected'),
]