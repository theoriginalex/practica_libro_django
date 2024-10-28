def crear_autor_simple():
  # Crear un autor

  from tu_app.models import Autor

  # Crear un nuevo autor
  nuevo_autor = Autor(nombre="Gabriel García Márquez")
  nuevo_autor.save()

  #--------------------------------------------------------
  #Asociar el autor con libros

  from tu_app.models import Libro

  # Obtener el libro existente
  libro_existente = Libro.objects.get(isbn="1234567890123")  # Cambia por el ISBN correcto

  # Asociar el autor al libro
  nuevo_autor.libro.add(libro_existente)

  #--------------------------------------------------------
  #Verificar la asociación
  # Obtener todos los libros asociados al autor
  libros_asociados = nuevo_autor.libros_autores.all()
  print(libros_asociados)
  
def insersion_masiva_de_autores():
  #Preparar la lista de autores
  from tu_app.models import Autor

  # Crear una lista de nuevos autores
  autores = [
      Autor(nombre="Gabriel García Márquez"),
      Autor(nombre="Julio Cortázar"),
      Autor(nombre="Isabel Allende"),
  ]
  # Insertar los autores en la base de datos
  Autor.objects.bulk_create(autores)

def consultar_registros():
  Autor.objects.all() 
  # Si conocemos la clave primaria del registro que estamos buscando podemos usar el método get.
  Libro.objects.get(isbn='1935182080')
  Libro.objects.get(pk='1935182080')
  # Si quisiéramos agregar nuestros propios métodos de búsqueda
  def buscar_por_isbn(self, isbn):
        try:
            return self.get(pk=isbn)
        except self.model.DoesNotExist:
            return f'No existe el libro {isbn}'
  # aqui se busca
  Libro.objects.buscar_por_isbn("1935182080")
  
  # Obtener solo el primer resultado
  Libro.objects.all().first()
  
  # Obtener solo el ultimo resultado
  Libro.objects.all().last()

  #Obtener los primeros N resultados
  "Ejemplo de obtener los primeros 5 libros"
  Libro.objects.all()[:5]

  #Consultar coincidencias por el inicio
  "Ejempo de obtener los libros cuyo isbn comience con un 16"
  Libro.objects.filter(isbn__startswith="16") 
  
  # Consultas por mayor que
  "Ejemplo de los libros que tienen mas de 200 paginas"
  Libro.objects.filter(paginas__gt=200) 
  
  # NOT IN
  f"Ejemplo de libros que tienen mas de 200 paginas pero cuyo isbn no sea ninguno de estos dos ('1933988592','1884777600')"
  Libro.objects.filter(paginas__gt=200).exclude(isbn__in=('1933988592','1884777600'))

  #Consultas por mayor o igual que
  "Ejemplo de libros que tienes 200 o mas paginas"
  Libro.objects.filter(paginas__gte=200)

  #Seleccionar las columnas a mostrar
  "Ejemplo de una consulta de los libros que tienen 200 o mas paginas, pero solo muestra las columnas isbn y paginas"
  Libro.objects.filter(paginas__gte=200).values('isbn','paginas')

  #Consultas por menor que
  "Ejemplo de los libros que tienen menos de 200 paginas"
  Libro.objects.filter(paginas__lt=200)

  #Consultas por menor o igual que
  "Ejemplo de libros que tienes 200 o menos paginas"
  Libro.objects.filter(paginas__lte=200)

  # Contar COUNT
  "Ejemplo de contar los libros que tienen menos de 200 paginas"
  Libro.objects.filter(paginas__lt=200).count() 
  
  #OR (forma larga)
  "Ejemplo de consulta de los libros con 200 paginas o con 300 paginas"
  consulta1 = Libro.objects.filter(paginas=200)
  consulta2 = Libro.objects.filter(paginas=300)(consulta1 | consulta2).values('isbn','paginas')
  
  # Consultar el por año de una fecha
  "Ejemplo de una consulta que muestra los libros cuya fecha de publicación es 2012"
  Libro.objects.filter(fecha_publicacion__year=2012).values('isbn','fecha_publicacion')

  # Filtrar usando expresiones regulares
  "Consultar los libros cuyo isbn comience con un 19 seguido de 8 digitos"
  Libro.objects.filter(isbn__regex=r'19\d{8}$').values('isbn')

  #UNION
  "Unir en una sola consulta el nombre los Autores que contengan la palabra hill con las Editoriales cuyo nombre contengatambién la palabra hill."
  a1 = Autor.objects.filter(nombre__contains='hill').values('nombre')
  e1 = Editorial.objects.filter(nombre__contains='hill').values('nombre')
  a1.union(e1)

  #El cuarto libro con mas paginas
  "Obtener el cuarto libro con mas paginas"
  Libro.objects.values('isbn','paginas').order_by('-paginas')[3]

  #El cuarto y quinto libro con mas paginas
  "Obtener el cuarto y quinto libro con mas paginas"
  Libro.objects.values('isbn','paginas').order_by('-paginas')[3:5]

def Paginando_a_mano():
  def LibroPorPaginas(self, pagina, filas_por_pagina=5):
        total_filas = self.count()
        total_paginas = math.ceil(total_filas / filas_por_pagina)
        final = pagina * filas_por_pagina
        inicial = final - filas_por_pagina
        print(f'Página {pagina} / {total_paginas}')
        return self.all().order_by('isbn')[inicial:final]
  #Usando la función podemos seleccionar por ejemplo la pagina 3
  Libro.objects.LibroPorPaginas(3)
  
  