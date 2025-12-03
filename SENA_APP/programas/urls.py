from django.urls import path
from . import views

urlpatterns = [
    path('Programas/', views.lista_programas, name='lista_programas'),
    path('Programa/<int:id_programa>/', views.detalle_programa, name='detalle_programa'),
]
