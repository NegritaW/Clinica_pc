from django.shortcuts import render, redirect
from functools import wraps
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from .forms import RegistrarUsuario
from django.contrib import messages

def login_view(request):
    """
    Login real usando Django auth.
    Si el usuario existe y está activo, inicia sesión.
    """
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Redirigir según rol o a protected
                return redirect('protected')
            else:
                # Usuario inactivo (pendiente de activación por admin)
                error = "Tu cuenta aún no ha sido activada. Contacta al administrador."
                return render(request, 'login.html', {'error': error})
        else:
            error = 'Usuario o clave incorrectos.'
            return render(request, 'login.html', {'error': error})
    # GET
    return render(request, 'login.html', {})


def logout_view(request):
    auth_logout(request)
    return redirect('home')


def session_required(view_func):
    """
    Decorador que protege vistas: requiere usuario autenticado y activo.
    Si no lo está, redirige al login.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_active:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


@session_required
def protected_view(request):
    """
    Vista protegida: muestra menú y opciones según rol del usuario.
    """
    user = request.user
    # Puedes ajustarlo para que muestre otras cosas por rol
    return render(request, 'protected.html', {'user_role': user.rol, 'user': user})


def register_view(request):
    """
    Registrar usuario con formulario UserCreationForm personalizado.
    Los usuarios quedan inactivos por defecto y el admin deberá activarlos.
    """
    if request.method == 'POST':
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # No activar automáticamente (ya lo maneja tu modelo is_active=False por defecto)
            user.is_active = False
            # No asignamos rol aquí (admin lo asigna después)
            user.rol = None
            user.save()
            messages.success(request, "Registro realizado. Espera a que el administrador active tu cuenta.")
            messages.success(request, "Ya puedes volver a login")
    else:
        form = RegistrarUsuario()
    return render(request, 'loginregistro.html', {'form': form})
