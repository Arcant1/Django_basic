from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^libros/$', views.LibroListView.as_view(), name='libros'),
    url(r'^libro/(?P<pk>\d+)$', views.LibroDetailView.as_view(), name='libro-detail'),
    url(r'^autores/$', views.AutorListView.as_view(), name='autores'),
    url(r'^autor/(?P<pk>\d+)$', views.AutorDetailView.as_view(), name='autor-detail'),

]
urlpatterns += [   
    url(r'^mislibros/$', views.LibrosPrestadosPorUsuarioListView.as_view(), name='mis-prestamos'),
]

urlpatterns += [   
    url(r'^libro/(?P<pk>[-\w]+)/renovar/$', views.renovar_libro_librarian, name='renovar-libro-librarian'),
]