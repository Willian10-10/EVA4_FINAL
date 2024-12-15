from django.urls import path
from . import views, api_views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),  # Redirige a landing_page
    path('landing/', views.landing_page, name='landing_page'),  # Página de inicio

    # Otras rutas
    path('crear/', views.crear_reserva, name='reserva_create'),
    path('editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reservas/nueva/', views.crear_reserva, name='crear_reserva'),
    path('eliminar_reserva/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    
    # Rutas de la API
    path('api/reservas/', api_views.ReservaList.as_view(), name='api_reservas_list'),
    path('api/reservas/<int:id>/', api_views.ReservaDetail.as_view(), name='api_reserva_detail'),
    path('reservas/', views.listar_reservas, name='reservas'),
]
