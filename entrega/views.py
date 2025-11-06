from django.shortcuts import render, redirect, get_object_or_404
from login.views import session_required
from django.contrib import messages
from .models import Entrega
from .forms import EntregaForm
from recepcion.models import Recepcion
from diagnostico.models import Diagnostico

@session_required
def verificar_equipo(request):
    equipos = Recepcion.objects.all()
    equipo = None
    nombre = request.GET.get("nombre")

    if nombre:
        equipo = get_object_or_404(Recepcion, id=nombre)
        entrega = Entrega.objects.filter(recepcion=equipo).first()
        diag = Diagnostico.objects.filter(recepcion=equipo).first()
    else:
        entrega = diag = None

    return render(request, "verificar.html", {
        "equipo": equipo,
        "equipos": equipos,
        "entrega": entrega,
        "diag": diag,
    })

@session_required
def reporte_entrega(request):
    if request.method == "POST":
        form = EntregaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrega registrada correctamente.")
            return redirect("comprobante", nombre=form.cleaned_data['recepcion'].id)
    else:
        form = EntregaForm()

    return render(request, "reporte.html", {"form": form})

@session_required
def comprobante(request, nombre):
    entrega = get_object_or_404(Entrega, recepcion_id=nombre)
    recepcion = entrega.recepcion
    diagnostico = Diagnostico.objects.filter(recepcion=recepcion).first()

    return render(request, "comprobante.html", {
        "entrega": entrega,
        "recepcion": recepcion,
        "diagnostico": diagnostico,
    })