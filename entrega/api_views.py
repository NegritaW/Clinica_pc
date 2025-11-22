from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Entrega
from .serializers import EntregaSerializer


# -------------------- GET - Listar entregas --------------------
@api_view(['GET'])
def api_lista_entregas(request):
    entregas = Entrega.objects.all()
    serializer = EntregaSerializer(entregas, many=True)
    return Response(serializer.data)


# -------------------- POST - Crear entrega --------------------
@api_view(['POST'])
def api_agregar_entrega(request):
    serializer = EntregaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------- PUT - Modificar entrega --------------------
@api_view(['PUT'])
def api_modificar_entrega(request, pk):
    try:
        entrega = Entrega.objects.get(pk=pk)
    except Entrega.DoesNotExist:
        return Response(
            {'error': 'Entrega no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = EntregaSerializer(entrega, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
