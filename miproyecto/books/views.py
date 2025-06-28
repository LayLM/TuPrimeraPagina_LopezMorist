from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import AutorForm, GeneroForm, LibroForm
from .models import Libro
from django.db.models import Q

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'books/crear_autor.html', {'form': form})

def crear_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_genero')
    else:
        form = GeneroForm()
    return render(request, 'books/crear_genero.html', {'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_libro')
    else:
        form = LibroForm()
    return render(request, 'books/crear_libro.html', {'form': form})

# Buscar libros por título o autor

from django import forms

class BuscarLibroForm(forms.Form):
    busqueda = forms.CharField(max_length=100, required=False, label='Buscar libro por título o autor')

def buscar_libro(request):
    form = BuscarLibroForm(request.GET or None)
    resultados = []
    if form.is_valid():
        texto = form.cleaned_data.get('busqueda')
        if texto:
            resultados = Libro.objects.filter(
                Q(titulo__icontains=texto) | Q(autor__nombre__icontains=texto)
            )
    return render(request, 'books/buscar_libro.html', {'form': form, 'resultados': resultados})

from django.shortcuts import render

# Books

def inicio(request):
    return render(request, 'books/inicio.html')
