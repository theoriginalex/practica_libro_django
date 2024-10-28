from django.db import models
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage
import math


# Validadores
def validar_titulo(titulo):
    if 'cobol' in titulo:
        raise ValidationError(f'{titulo} no se vende mucho')
    return titulo


# Managers personalizados
class LibroManager(models.Manager):
    def buscar_por_isbn(self, isbn):
        try:
            return self.get(pk=isbn)
        except self.model.DoesNotExist:
            return f'No existe el libro {isbn}'

    def LibroPorPaginas(self, pagina, filas_por_pagina=5):
        total_filas = self.count()
        total_paginas = math.ceil(total_filas / filas_por_pagina)
        final = pagina * filas_por_pagina
        inicial = final - filas_por_pagina
        print(f'Página {pagina} / {total_paginas}')
        return self.all().order_by('isbn')[inicial:final]

    def LibroPorPaginasDjango(self, pagina, filas_por_pagina=5):
        p = Paginator(self.all().order_by('isbn'), filas_por_pagina)
        print(f'Página {pagina} / {p.num_pages}')
        try:
            pag = p.page(pagina)
            return pag.object_list
        except EmptyPage:
            print("Página solicitada está fuera de rango.")
            return []


# Modelos
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'libreria_editorial'


class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=70, blank=True, validators=[validar_titulo])
    paginas = models.PositiveIntegerField()
    fecha_publicacion = models.DateField(null=True)
    imagen = models.URLField(max_length=85, null=True)
    desc_corta = models.CharField(max_length=2000)
    estatus = models.CharField(max_length=1)
    categoria = models.CharField(max_length=50)
    edicion_anterior = models.ForeignKey('self', null=True, default=None, on_delete=models.PROTECT)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    objects = LibroManager()
    paginas = models.PositiveIntegerField(db_index=True,)
    def __str__(self):
    
        return f'Yo soy {self.titulo}'

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(titulo='cobol'), name='titulo_no_permitido_chk')
        ]


class Autor(models.Model):
    nombre = models.CharField(max_length=70)
    libro = models.ManyToManyField(Libro, through='AutorCapitulo', related_name='libros_autores', through_fields=('autor', 'libro'))

    def __str__(self):
        return f'Yo soy {self.nombre}'


class LibroCronica(models.Model):
    descripcion_larga = models.TextField(null=True)
    libro = models.OneToOneField(Libro, on_delete=models.CASCADE, primary_key=True)


class AutorCapitulo(models.Model):
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    libro = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True)
    numero_capitulos = models.IntegerField(default=0)


# python manage.py shell_plus
# %load_ext autoreload
# %autoreload 2


#inprimir autores pag 50
"""
from django.db.models import Prefetch

# Prefetch de los libros a través de AutorCapitulo
autores = Autor.objects.prefetch_related(
    Prefetch('autorcapitulo_set', queryset=AutorCapitulo.objects.select_related('libro__editorial'))
)

for autor in autores:
    print(f'Autor: {autor}')
    print('Libros escritos:')
    for autor_capitulo in autor.autorcapitulo_set.all():  # Usando el nombre correcto
        libro = autor_capitulo.libro
        print(f'{libro.isbn} Editorial: {libro.editorial.nombre}')
"""


