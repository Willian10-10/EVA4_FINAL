from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'nombre', 'telefono', 'fecha', 'hora', 'cantidad_personas', 'estado', 'observacion']
