from django.db import models
from django.urls import reverse
import uuid					#	Se requiere para las instancias de libros únicos
from django.contrib.auth.models import User
from datetime import date

class Genero(models.Model):	#	Modelo que representa un género literario
		  
	nombre	=	models.CharField(max_length=200, help_text="Ingrese un género para el libro")

	def __str__(self):		#	Cadena que representa a la instancia particular del modelo
		
		return self.nombre

class Idioma(models.Model):
	LISTA_LENGUAJES = (
		('esp','Español'),
		('eng','English'),
		('esp','Esperanto')
	)
	leng = models.CharField(max_length=15, choices=LISTA_LENGUAJES, blank=True, default='esp', help_text="Lenguaje del libro")

	def __str__(self):
		return '%s' %(self.leng)

class Libro(models.Model):
	"""
	Modelo que representa un libro, pero no una instancia de dicho libro
	"""
	titulo = models.CharField(max_length=200)
	autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
	  # Foreign Key used because book can only have one author, but authors can have multiple books
	  # Author as a string rather than object because it hasn't been declared yet in file.
	descripcion = models.TextField(max_length=1000, help_text="Enter a brief description of the book",default="Sin descripción")
	isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genero = models.ManyToManyField(Genero, help_text="Select a genre for this book")
	lenguaje = models.ForeignKey('Idioma', on_delete=models.SET_NULL, null=True)
	  # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
	  # Genre class has already been defined so we can specify the object above.
	
	  
	def display_genre(self):
		"""
		Creates a string for the Genre. This is required to display genre in Admin.
		"""
		return ', '.join([ genero.nombre for genero in self.genero.all()[:3] ])
		display_genre.short_description = 'Genero'
	
	
	def get_absolute_url(self):
		"""
		Returns the url to access a particular book instance.
		"""
		return reverse('libro-detail', args=[str(self.id)])

	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return self.titulo
		

class	Instancia(models.Model):
	#	Modelo que representa una copia específica de un libro
	id		=	models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
	libro	=	models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True)
	imprint	=	models.CharField(max_length=200)
	fecha_en=	models.DateField(null=True, blank=True)
	usuario	=	models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	ESTADO_PRESTAMO	=	(
		('m','Mantenimiento'),
		('o','En prestamo'),
		('a','Disponible'),
		('r','Reservado')
	)
	estado = models.CharField(max_length=1, choices=ESTADO_PRESTAMO, blank=True, default='m', help_text="Estado de disponibilidad del libro")
	class Meta:
		ordering = ["fecha_en"]
	
	def __str__(self):
		#	String para representar el objeto del modelo
		return '%s (%s)' %(self.id, self.libro.titulo)
	
	@property
	def is_overdue(self):
		if self.fecha_en and date.today() > self.fecha_en :
			return True
		return False

class Autor(models.Model):
	#	Modelo que representa un autor
	nombre	=	models.CharField(max_length=100)
	apellido=	models.CharField(max_length=100)
	fecha_n =	models.DateField(null=True,	blank=True)
	fecha_d	=	models.DateField('Muerto',	null=True,	blank=True)

	def get_absolute_url(self):
		#	Devuelve la url para acceder a una instancia particular de un auto
		return reverse('autor-detail', args=[str(self.id)])

	def __str__(self):
		#	String para representar el objeto modelo
		return '%s, %s' %(self.apellido, self.nombre)
