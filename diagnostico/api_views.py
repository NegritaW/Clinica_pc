from rest_framework import generics
from .models import Diagnostico
from .serializers import DiagnosticoSerializer

class DiagnosticoListAPI(generics.ListCreateAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

class DiagnosticoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer