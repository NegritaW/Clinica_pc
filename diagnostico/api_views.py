from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Diagnostico
from .serializers import DiagnosticoSerializer

@api_view(['GET'])
def diagnostico_list_api(request):
    diagnosticos = Diagnostico.objects.all()
    serializer = DiagnosticoSerializer(diagnosticos, many=True)
    return Response(serializer.data)