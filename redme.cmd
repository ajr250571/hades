https://www.youtube.com/watch?v=XclfcvFjN48&list=PLxm9hnvxnn-j5ZDOgQS63UIBxQytPdCG7

Capitulo 30  4:13

Parámetros de objects.filter en Django
El método objects.filter() en Django te permite filtrar un conjunto de consultas ("QuerySet") por un conjunto de criterios. Los parámetros que puedes usar en este método son:

1. Filtros por campo:

Nombre del campo: Puedes filtrar por el valor exacto de un campo utilizando el nombre del campo como clave y el valor que deseas buscar como valor.
Ejemplo: objects.filter(nombre="Juan")

Operadores de comparación: Puedes usar operadores de comparación como __gt (mayor que), __lt (menor que), __gte (mayor o igual que), __lte (menor o igual que), __exact (igual a), __iexact (igual a ignorando mayúsculas y minúsculas), __contains (contiene), etc.
Ejemplo: objects.filter(edad__gt=18)

Filtros de cadena: Puedes usar filtros específicos para cadenas como __startswith (comienza con), __endswith (termina con), __icontains (contiene ignorando mayúsculas y minúsculas).
Ejemplo: objects.filter(nombre__startswith="A")

2. Filtros por relaciones:

Campos de relación: Puedes filtrar por objetos relacionados usando el nombre del campo de la relación seguido de __ y el nombre del campo del objeto relacionado.
Ejemplo: objects.filter(autor__nombre="Ana")

Filtros de búsqueda inversa: Puedes usar __in para filtrar por objetos que están relacionados con un conjunto de otros objetos.
Ejemplo: objects.filter(autor__in=Autor.objects.filter(pais="Argentina"))

3. Filtros avanzados:

Q objects: Puedes usar Q objects para combinar múltiples criterios de filtro en una sola consulta.
Ejemplo: objects.filter(Q(nombre="Juan") | Q(edad__gt=18))

Expresiones F: Puedes usar expresiones F para realizar comparaciones con valores dinámicos.
Ejemplo: objects.filter(edad__gt=F('salario') * 0.1)

4. Otros parámetros:

exclude: Puedes usar exclude para excluir objetos que coincidan con un conjunto de criterios.
Ejemplo: objects.exclude(nombre="Juan")

order_by: Puedes usar order_by para ordenar los resultados de la consulta.
Ejemplo: objects.filter(nombre="Juan").order_by('-edad')

limit: Puedes usar limit para limitar el número de resultados que se devuelven.
Ejemplo: objects.filter(nombre="Juan").limit(10)