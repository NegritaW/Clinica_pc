from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.html import format_html
from login.views import session_required
from .forms import RecepcionForm
from .models import Recepcion


@session_required
def registrar_equipo(request):
    """Registrar una nueva recepción de equipo"""
    if request.method == 'POST':
        form = RecepcionForm(request.POST)
        if form.is_valid():
            form.save()
            cliente = form.cleaned_data['cliente']
            messages.success(request, f"Equipo de {cliente} registrado correctamente.")
            messages.success(request, format_html(
                'Ahora puedes diagnosticarlo en <a href="{}">Diagnóstico</a>', '/diagnostico/listado'
            ))
            return redirect('listado_equipos')
        else:
            messages.error(request, "Corrige los errores antes de continuar.")
    else:
        form = RecepcionForm()

    return render(request, 'registrar.html', {'form': form})


@session_required
def listado_equipos(request):
    """Mostrar todas las recepciones registradas"""
    equipos = Recepcion.objects.select_related('cliente', 'recepcionista').order_by('-fecha_recepcion')
    return render(request, 'listado.html', {'equipos': equipos})


@session_required
def detalle_equipo(request, nombre):
    """Mostrar detalle de una recepción específica (por nombre del cliente)"""
    equipo = get_object_or_404(Recepcion, cliente__nombre_completo=nombre)
    return render(request, 'detalle.html', {'equipo': equipo})
