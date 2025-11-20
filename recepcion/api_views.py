from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Recepcion
from .serializers import RecepcionSerializer

@api_view(['GET'])
def recepcion_list_api(request):
    recepcion = Recepcion.objects.all()
    serializer = RecepcionSerializer(recepcion, many=True)
    return Response(serializer.data)