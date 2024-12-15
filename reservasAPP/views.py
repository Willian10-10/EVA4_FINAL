from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm



def index(request):
    return render(request, 'index.html')

def listar_reservas(request):
    reservas = Reserva.objects.all()  # Obtiene todas las reservas
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def index(request):
    reservas = Reserva.objects.all()  # Obtiene todas las reservas
    return render(request, 'index.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')  # Redirige a la página de reservas
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