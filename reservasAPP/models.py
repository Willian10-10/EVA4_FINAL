from django.db import models

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='RESERVADO')
    observacion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Reserva de {self.nombre} para {self.cantidad_personas} personas el {self.fecha}"
