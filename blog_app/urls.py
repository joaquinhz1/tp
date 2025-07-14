from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_entrada/', views.agregar_entrada, name='agregar_entrada'),
    path('buscar/', views.buscar, name='buscar'),
]
