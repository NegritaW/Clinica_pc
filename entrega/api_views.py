from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Entrega
from .serializers import EntregaSerializer


@api_view(['GET'])
def entrega_list_api(request):
    entregas = Entrega.objects.all()
    serializer = EntregaSerializer(entregas, many=True)
    return Response(serializer.data)
