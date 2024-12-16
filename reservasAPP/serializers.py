from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'nombre', 'telefono', 'fecha', 'hora', 'cantidad_personas', 'estado', 'observacion']

    def validate_cantidad_personas(self, value):
        if value < 1 or value > 15:
            raise serializers.ValidationError("La cantidad de personas debe estar entre 1 y 15.")
        return value
