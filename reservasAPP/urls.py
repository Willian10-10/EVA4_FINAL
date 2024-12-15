from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('crear/', views.crear_reserva, name='reserva_create'),  # Ruta para crear una reserva
    path('editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),  # Ruta para editar una reserva
    path('reservas/', views.listar_reservas, name='listar_reservas'),  # Listar reservasz
    path('reservas/nueva/', views.crear_reserva, name='crear_reserva'),  # Ruta para crear una reserva
]
