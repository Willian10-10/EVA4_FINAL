from django.urls import path
from . import api_views

urlpatterns = [
    path('reservas/', api_views.ReservaListCreateView.as_view(), name='reservas_api'),
    path('reservas/<int:pk>/', api_views.ReservaRetrieveUpdateDeleteView.as_view(), name='reserva_detail_api'),
]
