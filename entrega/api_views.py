from rest_framework import generics
from .models import Entrega
from .serializers import EntregaSerializer

class EntregaListAPI(generics.ListCreateAPIView):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

class EntregaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer