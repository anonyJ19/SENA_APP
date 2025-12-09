from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.aprendiz, name='lista_aprendices'),
    path('aprendices/aprendiz/<int:id_aprendiz>/', views.detalle_aprendiz, name='detalle_aprendiz'),
    path('crear/', views.AprendizCreateView.as_view(), name='crear_aprendiz'),
    path('editar/aprendiz/<str:documento>/', views.AprendizUpdateView.as_view(), name='editar_aprendiz'),
    path('aprendices/<int:documento>/eliminar/', views.AprendizDeleteView.as_view(), name='eliminar_aprendiz')


]