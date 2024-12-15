from rest_framework import generics
from .models import Reserva
from .serializers import ReservaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ReservaListCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all().order_by('fecha')
    serializer_class = ReservaSerializer

class ReservaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer



class ReservaList(APIView):
    # Obtener todas las reservas
    def get(self, request):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

    # Crear una nueva reserva
    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservaDetail(APIView):
    # Obtener una reserva por ID
    def get(self, request, id):
        try:
            reserva = Reserva.objects.get(id=id)
        except Reserva.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)

    # Modificar una reserva existente
    def put(self, request, id):
        try:
            reserva = Reserva.objects.get(id=id)
        except Reserva.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar una reserva
    def delete(self, request, id):
        try:
            reserva = Reserva.objects.get(id=id)
        except Reserva.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)