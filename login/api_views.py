from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer


# -------------------- GET - Listar usuarios --------------------
@api_view(['GET'])
def api_lista_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)


# -------------------- POST - Crear usuario --------------------
@api_view(['POST'])
def api_agregar_usuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------- PUT - Modificar usuario --------------------
@api_view(['PUT'])
def api_modificar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(
            {'error': 'Usuario no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------- DELETE - Eliminar Usuario --------------------
@api_view(['DELETE'])
def api_eliminar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'},
        status=status.HTTP_404_NOT_FOUND)
    
    usuario.delete()
    return Response({'mensaje': 'Usuario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)