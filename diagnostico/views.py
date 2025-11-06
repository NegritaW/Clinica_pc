from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from login.views import session_required
from .models import Diagnostico
from .forms import DiagnosticoForm
from recepcion.models import Recepcion
from entrega.models import Entrega

@session_required
def listado_diagnosticos(request):
    diagnosticos = Diagnostico.objects.select_related('recepcion', 'tecnico').all()
    entregados = Entrega.objects.values_list('recepcion_id', flat=True)
    equipos_sin_diag = Recepcion.objects.exclude(id__in=diagnosticos.values_list('recepcion_id', flat=True))

    return render(request, "listado_diagnosticos.html", {
        "diagnosticos": diagnosticos,
        "equipos_sin_diag": equipos_sin_diag,
        "entregados": entregados,
    })

@session_required
def evaluar_equipo(request):
    recepcion_id = request.GET.get("nombre")  # Usar 'nombre' como ID de Recepcion
    recepcion = get_object_or_404(Recepcion, id=recepcion_id)

    diagnostico, created = Diagnostico.objects.get_or_create(recepcion=recepcion)

    if request.method == "POST":
        form = DiagnosticoForm(request.POST, instance=diagnostico)
        if form.is_valid():
            form.save()
            messages.success(request, "Diagnóstico guardado correctamente.")
            return redirect("diagnostico_listado")
    else:
        form = DiagnosticoForm(instance=diagnostico)

    return render(request, "evaluar.html", {
        "form": form,
        "recepcion": recepcion,
        "nombre_equipo": recepcion_id,
    })

@session_required
def eliminar_diagnostico(request, nombre):
    diagnostico = get_object_or_404(Diagnostico, recepcion_id=nombre)
    diagnostico.delete()
    messages.success(request, "Diagnóstico eliminado correctamente.")
    return redirect("diagnostico_listado")
