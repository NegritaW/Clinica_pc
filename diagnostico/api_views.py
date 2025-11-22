from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Diagnostico
from .serializers import DiagnosticoSerializer


# -------------------- GET - Listar diagnósticos --------------------
@api_view(['GET'])
def api_lista_diagnosticos(request):
    diagnosticos = Diagnostico.objects.all()
    serializer = DiagnosticoSerializer(diagnosticos, many=True)
    return Response(serializer.data)


# -------------------- POST - Crear diagnóstico --------------------
@api_view(['POST'])
def api_agregar_diagnostico(request):
    serializer = DiagnosticoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------- PUT - Modificar diagnóstico --------------------
@api_view(['PUT'])
def api_modificar_diagnostico(request, pk):
    try:
        diagnostico = Diagnostico.objects.get(pk=pk)
    except Diagnostico.DoesNotExist:
        return Response(
            {'error': 'Diagnóstico no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = DiagnosticoSerializer(diagnostico, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)