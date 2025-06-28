from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Books
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_genero/', views.crear_genero, name='crear_genero'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
]
