from rest_framework import generics
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaListCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all().order_by('fecha')
    serializer_class = ReservaSerializer

class ReservaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
