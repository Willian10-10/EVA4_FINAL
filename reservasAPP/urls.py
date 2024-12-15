from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
]
