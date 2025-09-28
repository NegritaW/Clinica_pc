from django.shortcuts import render, redirect
from login.views import session_required
from recepcion.views import equipos_registrados

# Simulación: lista de entregas
entregas = []

@session_required
def verificar_equipo(request):
    equipo = None
    nombre = request.GET.get("nombre")
    if nombre:
        equipo = next((e for e in equipos_registrados if e["nombre"] == nombre), None)
        entrega_info = next((en for en in entregas if en["nombre"] == nombre), None)
        if entrega_info:
            equipo = {**equipo, **entrega_info}
        # buscar también si tiene estudiante asignado en diagnósticos
        from diagnostico.views import diagnosticos
        diag = next((d for d in diagnosticos if d["nombre"] == nombre), None)
        if diag:
            equipo["estudiante"] = diag["estudiante"]

    return render(request, "verificar.html", {
        "equipo": equipo,
        "equipos": equipos_registrados,
    })

@session_required
def reporte_entrega(request):
    nombre = request.GET.get("nombre") or request.POST.get("nombre")
    mensaje = None
    mensaje_tipo = None  # para colorear el mensaje en el template

    if request.method == "POST":
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

            # mensaje de confirmación según el estado
            if estado == "entregado":
                mensaje = f"✅ El equipo de {nombre} fue marcado como ENTREGADO correctamente."
                mensaje_tipo = "success"
            elif estado == "pendiente":
                mensaje = f"⚠️ El equipo de {nombre} quedó en estado PENDIENTE."
                mensaje_tipo = "warning"
            else:
                mensaje = f"❌ El equipo de {nombre} fue marcado como {estado.upper()}."
                mensaje_tipo = "error"

            return redirect("comprobante", nombre=nombre)
        else:
            mensaje = "El cliente no existe en recepción."
            mensaje_tipo = "error"

    return render(request, "reporte.html", {
        "mensaje": mensaje,
        "mensaje_tipo": mensaje_tipo,
        "nombre": nombre
    })

@session_required
def comprobante(request, nombre):
    equipo = next((e for e in entregas if e["nombre"] == nombre), None)
    if equipo:
        # recuperar equipo base
        base = next((e for e in equipos_registrados if e["nombre"] == nombre), None)
        if base:
            equipo = {**base, **equipo}

        # buscar estudiante asignado en diagnósticos
        from diagnostico.views import diagnosticos
        diag = next((d for d in diagnosticos if d["nombre"] == nombre), None)
        if diag:
            equipo["estudiante"] = diag["estudiante"]

    return render(request, "comprobante.html", {"equipo": equipo})