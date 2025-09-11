from django.shortcuts import render, redirect

# Credenciales fijas
VALID_USERNAME = 'inacap'
VALID_PASSWORD = 'clinica2025'

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            request.session['autenticado'] = True
            return redirect('/recepcion/registrar/')
        else:
            error = 'Usuario o clave incorrectos.'
    return render(request, 'login.html', {'error': error})

def logout_view(request):
    request.session.pop('autenticado', None)
    return redirect('login:login')

# Decorador para proteger vistas
def session_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('autenticado', False):
            return redirect('login:login')
        return view_func(request, *args, **kwargs)
    return wrapper

@session_required
def protected_view(request):
    return render(request, 'protected.html', {})