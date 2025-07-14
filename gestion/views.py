from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, LibroForm, LibroSearchForm
from .models import Libro

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_libros')
    return render(request, 'gestion/autor_form.html', {'form': form})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_libros')
    return render(request, 'gestion/categoria_form.html', {'form': form})

def crear_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_libros')
    return render(request, 'gestion/libro_form.html', {'form': form})

def buscar_libro(request):
    form = LibroSearchForm(request.GET or None)
    libros = None
    if form.is_valid():
        titulo = form.cleaned_data['titulo']
        libros = Libro.objects.filter(titulo__icontains=titulo)
    return render(request, 'gestion/libro_search.html', {'form': form, 'libros': libros})

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestion/libro_list.html', {'libros': libros})
