from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usuario
from .serializers import UsuarioSerializer


@api_view(['GET'])
def usuario_list_api(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)