from django.shortcuts import render, redirect
from .models import Entrada
from .forms import AutorForm, CategoriaForm, EntradaForm

def home(request):
    entradas = Entrada.objects.all()
    return render(request, 'home.html', {'entradas': entradas})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Agregar Autor'})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Agregar Categoria'})

def agregar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntradaForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Agregar Entrada'})

def buscar(request):
    query = request.GET.get('q')
    resultados = Entrada.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})
