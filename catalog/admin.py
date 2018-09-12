from django.contrib import admin

from .models import Autor, Genero, Libro, Instancia, Idioma

#admin.site.register(Libro)
admin.site.register(Genero)
#admin.site.register(Autor)
#admin.site.register(Instancia)
admin.site.register(Idioma)
# Register your models here.

class InstanciaInline(admin.TabularInline):
	model=Instancia
	
class LibroInline(admin.TabularInline):
	model=Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
	list_display=('apellido', 'nombre', 'fecha_n', 'fecha_d')
	fields=['nombre','apellido',('fecha_n','fecha_d')]
	LibroInline.extra=0
	inlines = [LibroInline]

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
	list_display=('titulo','autor','display_genre')
	InstanciaInline.extra=0 			#Para no mostrar instancias extra
	inlines = [InstanciaInline]


@admin.register(Instancia)
class InstanciaAdmin(admin.ModelAdmin):
	list_filter=('estado','fecha_en')
	list_display=('libro','estado','usuario','fecha_en','id')
	fieldsets=(
		(None,{
			'fields':('libro','imprint','id')
		}),
		('Disponibilidad',{
			'fields':('estado','fecha_en','usuario')
		}),
	)
