# reservasAPP/api_urls.py

from django.urls import path
from .api_views import ReservaList, ReservaDetail

urlpatterns = [
    path('reservas/', ReservaList.as_view(), name='reservas_list'),  # Ruta para obtener todas las reservas o crear una nueva
    path('reservas/<int:id>/', ReservaDetail.as_view(), name='reserva_detail'),  # Ruta para obtener, editar o eliminar una reserva por ID
]
