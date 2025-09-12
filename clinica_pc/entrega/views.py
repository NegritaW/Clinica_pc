from django.shortcuts import render, redirect
from login.views import session_required
from recepcion.views import equipos_registrados

# Simulación: lista de entregas
entregas = []

@session_required
def verificar_equipo(request):
    equipo = None
    if request.method == "GET":
        nombre = request.GET.get("nombre")
        if nombre:
            equipo = next((e for e in equipos_registrados if e["nombre"] == nombre), None)
            entrega_info = next((en for en in entregas if en["nombre"] == nombre), None)
            if entrega_info:
                equipo = {**equipo, **entrega_info}  # combina datos

    return render(request, "verificar.html", {"equipo": equipo})
@session_required
def reporte_entrega(request):
    mensaje = None
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        estado = request.POST.get("estado")
        observaciones = request.POST.get("observaciones")
        equipo = next((e for e in equipos_registrados if e["nombre"] == nombre), None)
        if equipo:
            entrega = {
                "nombre": nombre,
                "estado": estado,
                "observaciones": observaciones,
            }
            entregas[:] = [e for e in entregas if e["nombre"] != nombre]
            entregas.append(entrega)

            return redirect("comprobante", nombre=nombre)
        else:
            mensaje = "El cliente no existe en recepción."

    return render(request, "reporte.html", {"mensaje": mensaje})

@session_required
def comprobante(request, nombre):
    equipo = next((e for e in equipos_registrados if e["nombre"] == nombre), None)
    entrega_info = next((en for en in entregas if en["nombre"] == nombre), None)
    if equipo and entrega_info:
        equipo = {**equipo, **entrega_info}
    return render(request, "comprobante.html", {"equipo": equipo})