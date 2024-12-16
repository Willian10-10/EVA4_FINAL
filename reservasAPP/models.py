from django.db import models

class Reserva(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    fecha = models.DateField(verbose_name="Fecha de la Reserva")
    hora = models.TimeField(verbose_name="Hora de la Reserva")
    cantidad_personas = models.PositiveIntegerField(verbose_name="Cantidad de Personas")
    estado = models.CharField(max_length=15, choices=ESTADOS, verbose_name="Estado")
    observacion = models.TextField(blank=True, null=True, verbose_name="Observación")  # Opcional

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.cantidad_personas < 1 or self.cantidad_personas > 15:
            raise ValidationError("La cantidad de personas debe estar entre 1 y 15.")
    
    def __str__(self):
        return f"Reserva de {self.nombre} para {self.cantidad_personas} personas el {self.fecha} a las {self.hora}."


