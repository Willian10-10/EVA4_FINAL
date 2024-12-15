from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'telefono', 'fecha', 'hora', 'cantidad_personas', 'estado', 'observacion']
    
    def clean_cantidad_personas(self):
        cantidad = self.cleaned_data.get('cantidad_personas')
        if cantidad < 1 or cantidad > 15:
            raise forms.ValidationError("La cantidad de personas debe estar entre 1 y 15.")
        return cantidad
