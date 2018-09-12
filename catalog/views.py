from django.shortcuts import render
from .models import Libro, Autor, Instancia, Genero
from django.views import generic

# Create your views here.

def index(request):
    #Función VISTA para la página de inicio del sitio
    #Genera contadores de algunos de los objetos principales
    num_libros = Libro.objects.all().count()
    num_instancias= Instancia.objects.all().count()
    num_instancias_disponibles=Instancia.objects.filter(estado__exact='a').count() #WARDA
    num_autores= Autor.objects.all().count()
    num_generos = Genero.objects.all().count()
    num_libros_darya = Libro.objects.filter(titulo__icontains='Darya').count() #isensitive case
    return render(
        request,
        'index.html',
        context={
            'num_libros':num_libros,
            'num_instancias':num_instancias,
            'num_instancias_disponibles':num_instancias_disponibles,
            'num_autores':num_autores,
            'num_generos':num_generos,
            'num_libros_darya':num_libros_darya,
            },
    )

class LibroListView(generic.ListView):
    model = Libro
    paginate_by = 5

    #def get_queryset(self):
    #    return Libro.objects.filter(titulo__icontains='de')[:5]

    def get_context_data(self, **kwargs):
        context = super(LibroListView, self).get_context_data(**kwargs)
        context['some data'] = 'Esto son solo datos'
        return context

class LibroDetailView(generic.DetailView):
    model = Libro

class AutorListView(generic.ListView):
    model = Autor
    paginate_by = 3

class AutorDetailView(generic.DetailView):
    model = Autor