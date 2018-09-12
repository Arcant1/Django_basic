from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^libros/$', views.LibroListView.as_view(), name='libros'),
    url(r'^libro/(?P<pk>\d+)$', views.LibroDetailView.as_view(), name='libro-detail')
]
