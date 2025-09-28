from django.shortcuts import render, redirect, HttpResponse
from functools import wraps

VALID_USERNAME = 'inacap'
VALID_PASSWORD = 'clinica2025'

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # guardar la sesión
            request.session['autenticado'] = True
            # debug: muestra en consola del servidor el contenido de la sesión
            print("SESSION after login:", dict(request.session.items()))
            # redirigir a protegido
            return redirect('protected')
        else:
            error = 'Usuario o clave incorrectos.'
    return render(request, 'login.html', {'error': error})

def logout_view(request):
    # limpiar sesión
    request.session.flush()
    return redirect('home')  # o 'login' si prefieres

def session_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # debug: imprimir estado de sesión en consola
        print("SESSION on protected check:", dict(request.session.items()))
        if not request.session.get('autenticado', False):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

@session_required
def protected_view(request):
    return render(request, 'protected.html')
