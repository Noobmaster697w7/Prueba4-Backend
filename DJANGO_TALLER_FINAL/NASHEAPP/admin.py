from django.contrib import admin
from NASHEAPP.models import Alumnos, Institucion

class AlumnosAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(Alumnos, AlumnosAdmin)    

# Register your models here.
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(Institucion, AlumnosAdmin)