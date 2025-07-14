from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autor/nuevo/', views.crear_autor, name='crear_autor'),
    path('categoria/nuevo/', views.crear_categoria, name='crear_categoria'),
    path('libro/nuevo/', views.crear_libro, name='crear_libro'),
    path('libro/buscar/', views.buscar_libro, name='buscar_libro'),
    path('', views.listar_libros, name='listar_libros'),
]
