from django.contrib import admin
from core.models import Usuarios
from core.models import Categorias


# Register your models here.

class usuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre","email","descripcion")



admin.site.register(Usuarios,usuarioAdmin)

class categAdmin(admin.ModelAdmin):
    list_display = ("desarrollo","investigacion")



admin.site.register(Categorias,categAdmin)