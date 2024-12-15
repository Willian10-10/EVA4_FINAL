from django.urls import path
from . import views, api_views

urlpatterns = [
    # Rutas para la interfaz web
    path('', views.index, name='index'),  # Página principal
    path('crear/', views.crear_reserva, name='reserva_create'),  # Ruta para crear una reserva
    path('editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),  # Ruta para editar una reserva
    path('reservas/', views.listar_reservas, name='listar_reservas'),  # Listar reservas
    path('reservas/nueva/', views.crear_reserva, name='crear_reserva'),  # Ruta para crear una reserva
    path('eliminar_reserva/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    
    # Rutas de la API (para la administración de reservas)
    path('api/reservas/', api_views.ReservaList.as_view(), name='api_reservas_list'),  # Listar todas las reservas o crear
    path('api/reservas/<int:id>/', api_views.ReservaDetail.as_view(), name='api_reserva_detail'),  # Detalle, editar o eliminar una reserva
]
