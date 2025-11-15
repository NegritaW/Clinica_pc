from rest_framework import generics
from .models import Recepcion
from .serializers import RecepcionSerializer

class RecepcionListAPI(generics.ListCreateAPIView):
    queryset = Recepcion.objects.all()
    serializer_class = RecepcionSerializer

class RecepcionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recepcion.objects.all()
    serializer_class = RecepcionSerializer