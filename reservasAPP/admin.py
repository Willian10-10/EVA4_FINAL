from django.contrib import admin
from .models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'fecha', 'hora', 'cantidad_personas', 'estado')  # Campos que se mostrarán en la lista
    list_filter = ('fecha', 'estado')  # Filtros laterales por fecha y estado
    search_fields = ('nombre', 'telefono')  # Búsqueda por nombre o teléfono
    ordering = ('-fecha', 'hora')  # Ordenar por fecha descendente y hora ascendente

# Registrar el modelo y la configuración personalizada
admin.site.register(Reserva, ReservaAdmin)
