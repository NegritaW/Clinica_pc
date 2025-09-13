from django.shortcuts import render, redirect
from django.urls import reverse
from login.views import session_required
from recepcion.views import equipos_registrados   # importamos la lista en memoria

# Lista en memoria de diagnósticos (simulada)
diagnosticos = []

ESTUDIANTES = [
    "Juan Pérez",
    "María López",
    "Carlos Díaz",
    "Ana Torres"
]
@session_required
def asignar_equipo(request):
    """
    GET: muestra formulario con lista de equipos disponibles y campo estudiante.
    POST: asigna el equipo al estudiante (crea entrada 'asignado' en diagnosticos) 
          y redirige a la vista de evaluar con query param ?nombre=...
    """
    mensaje = None
    if request.method == 'POST':
        estudiante = request.POST.get('estudiante', '').strip()
        nombre = request.POST.get('equipo', '').strip()

        equipo = next((e for e in equipos_registrados if e['nombre'] == nombre), None)
        if not estudiante or not equipo:
            mensaje = "Complete estudiante y seleccione un equipo válido."
        else:
            # crear registro de diagnóstico (estado: asignado)
            registro = {
                'nombre': equipo['nombre'],
                'tipo': equipo['tipo'],
                'problema': equipo['problema'],
                'estudiante': estudiante,
                'diagnostico': '',
                'solucion': '',
                'estado': 'asignado',
            }
            diagnosticos.append(registro)
            # redirigir a evaluar con el nombre del equipo en querystring
            return redirect(reverse('diagnostico_evaluar') + f'?nombre={equipo["nombre"]}')
    # GET: mostrar formulario
    return render(request, 'asignar.html', {'equipos': equipos_registrados, 'mensaje': mensaje})


@session_required
def evaluar_equipo(request):
    nombre_equipo = request.GET.get("nombre")
    diag = next((d for d in diagnosticos if d["nombre"] == nombre_equipo), None)

    if request.method == "POST":
        estudiante = request.POST.get("estudiante", "").strip()
        diagnostico_txt = request.POST.get("diagnostico", "").strip()
        solucion = request.POST.get("solucion", "").strip()
        estado = request.POST.get("estado", "asignado")

        if diag:
            diag["estudiante"] = estudiante
            diag["diagnostico"] = diagnostico_txt
            diag["solucion"] = solucion
            diag["estado"] = estado
        else:
            nuevo = {
                "nombre": nombre_equipo,
                "estudiante": estudiante,
                "diagnostico": diagnostico_txt,
                "solucion": solucion,
                "estado": estado,
            }
            diagnosticos.append(nuevo)

        return redirect("diagnostico_listado")

    return render(request, "evaluar.html", {
        "equipo": diag,
        "nombre_equipo": nombre_equipo,
        "estudiantes": ESTUDIANTES,  # 👈 pasamos la lista
    })

@session_required
def listado_diagnosticos(request):
    # Buscar qué equipos no tienen diagnóstico asignado
    nombres_diagnosticados = [d["nombre"] for d in diagnosticos]
    equipos_sin_diag = [e for e in equipos_registrados if e["nombre"] not in nombres_diagnosticados]

    return render(request, "listado_diagnosticos.html", {
        "diagnosticos": diagnosticos,
        "equipos_sin_diag": equipos_sin_diag,
    })

@session_required
def eliminar_diagnostico(request, nombre):
    global diagnosticos
    diagnosticos = [d for d in diagnosticos if d["nombre"] != nombre]
    return redirect("diagnostico_listado")
