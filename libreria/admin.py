from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Autor)
admin.site.register(models.AutorCapitulo)
admin.site.register(models.Editorial)
admin.site.register(models.Libro)
admin.site.register(models.LibroCronica)


