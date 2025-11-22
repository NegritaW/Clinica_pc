from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Recepcion
from .serializers import RecepcionSerializer


# -------------------- GET - Listar recepciones --------------------
@api_view(['GET'])
def api_lista_recepciones(request):
    recepciones = Recepcion.objects.all()
    serializer = RecepcionSerializer(recepciones, many=True)
    return Response(serializer.data)


# -------------------- POST - Crear recepción --------------------
@api_view(['POST'])
def api_agregar_recepcion(request):
    serializer = RecepcionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------- PUT - Modificar recepción --------------------
@api_view(['PUT'])
def api_modificar_recepcion(request, pk):
    try:
        recepcion = Recepcion.objects.get(pk=pk)
    except Recepcion.DoesNotExist:
        return Response(
            {'error': 'Recepción no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = RecepcionSerializer(recepcion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)