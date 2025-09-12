from django.shortcuts import render, redirect
from login.views import session_required

# Lista simulada de equipos (diccionarios)
equipos_registrados = []

@session_required
def registrar_equipo(request):
    mensaje = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        problema = request.POST.get('problema')

        if nombre and tipo and problema:
            equipo = {
                'nombre': nombre,
                'tipo': tipo,
                'problema': problema,
            }
            equipos_registrados.append(equipo)
            mensaje = f"Equipo de {nombre} registrado correctamente."
        else:
            mensaje = "Todos los campos son obligatorios."

    return render(request, 'registrar.html', {'mensaje': mensaje})

@session_required
def listado_equipos(request):
    return render(request, 'listado.html', {'equipos': equipos_registrados})

@session_required
def detalle_equipo(request, nombre):
    equipo = next((e for e in equipos_registrados if e['nombre'] == nombre), None)
    return render(request, 'detalle.html', {'equipo': equipo})