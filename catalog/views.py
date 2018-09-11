from django.shortcuts import render
from .models import Libro, Autor, Instancia, Genero

# Create your views here.

def index(request):
    #Función VISTA para la página de inicio del sitio
    #Genera contadores de algunos de los objetos principales
    num_libros = Libro.objects.all().count()
    num_instancias= Instancia.objects.all().count()
    num_instancias_disponibles=Instancia.objects.filter(estado__exact='a').count() #WARDA
    num_autores= Autor.objects.all().count()
    return render(
        request,
        'index.html',
        context={
            'num_libros':num_libros,
            'num_instancias':num_instancias,
            'num_instancias_disponibles':num_instancias_disponibles,
            'num_autores':num_autores
            },
    )
