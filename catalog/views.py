from django.shortcuts import render
from .models import Libro, Autor, Instancia, Genero
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def index(request):
    #Función VISTA para la página de inicio del sitio
    #Genera contadores de algunos de los objetos principales

    #Contador de visitas

    num_visitas = request.session.get('num_visitas',0)
    request.session['num_visitas'] = num_visitas+1

    #Parte de la biblioteca
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
            'num_visitas':num_visitas #agregado
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

class GeneroListView(generic.ListView):
    model = Genero

class LibroDetailView(generic.DetailView):
    model = Libro

class AutorListView(generic.ListView):
    model = Autor
    paginate_by = 3

class AutorDetailView(generic.DetailView):
    model = Autor

class LibrosPrestadosPorUsuarioListView(LoginRequiredMixin,generic.ListView):
    """
    Vista genérica basada en clases para listar los libros en préstamo al usuario actual
    """
    model = Instancia
    template_name = 'catalog/lista_instancia_prestadas_user.html'
    paginate_by = 1

    def get_queryset(self):
        return Instancia.objects.filter(usuario=self.request.user).filter(estado__exact='o').order_by('fecha_en')

from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenovarLibroForm

@permission_required('catalog.puede_marcar_retornado')
def renovar_libro_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    
    book_inst=get_object_or_404(Instancia, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenovarLibroForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.fecha_en = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenovarLibroForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})