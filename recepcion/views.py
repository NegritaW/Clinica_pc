from django.shortcuts import render, redirect
from django.contrib import messages
from login.views import session_required

# Lista simulada de equipos (diccionarios)
equipos_registrados = []

@session_required
def registrar_equipo(request):
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
            # ✅ usamos messages y redirigimos
            messages.success(request, f"Equipo de {nombre} registrado correctamente.")
            messages.success(request, "Ahora puedes diagnosticarlo en 'Diagnóstico'.")
            return redirect('listado_equipos')
        else:
            messages.error(request, "Todos los campos son obligatorios.")

    return render(request, 'registrar.html')  # sin pasar mensaje directo


@session_required
def listado_equipos(request):
    return render(request, 'listado.html', {'equipos': equipos_registrados})


@session_required
def detalle_equipo(request, nombre):
    equipo = next((e for e in equipos_registrados if e['nombre'] == nombre), None)
    return render(request, 'detalle.html', {'equipo': equipo})