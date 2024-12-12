from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora', 'cantidad_personas', 'estado')
    search_fields = ('nombre', 'telefono', 'estado')
    list_filter = ('estado', 'fecha')
