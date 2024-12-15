from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm
from django import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReservaSerializer

def index(request):
    return render(request, 'index.html')
def landing_page(request):
    return render(request, 'landing_page.html')

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def index(request):
    reservas = Reserva.objects.all()  # Obtiene todas las reservas
    return render(request, 'index.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')  # Redirige al listado de reservas
    else:
        form = ReservaForm()

    return render(request, 'crear_reserva.html', {'form': form})
def editar_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige al index después de editar la reserva
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'editar_reserva.html', {'form': form, 'reserva': reserva})

def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    
    if request.method == 'POST':
        reserva.delete()
        return redirect('listar_reservas')  # Redirigir al listado de reservas
    
    return render(request, 'eliminar_reserva.html', {'reserva': reserva})


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'telefono', 'fecha', 'hora', 'cantidad_personas', 'estado', 'observacion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_cantidad_personas(self):
        cantidad_personas = self.cleaned_data.get('cantidad_personas')
        if cantidad_personas < 1 or cantidad_personas > 15:
            raise forms.ValidationError("La cantidad de personas debe estar entre 1 y 15.")
        return cantidad_personas
    



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