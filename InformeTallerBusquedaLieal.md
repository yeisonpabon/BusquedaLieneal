UNIVERSIDAD DEL VALLE

Programa: Tecnología en Desarrollo de Software

Asignatura: Análisis y Diseño de Algoritmos

Taller — Búsqueda Lineal
YEISON ANDRES VILLEGAS PABON


Introducción

El taller de Búsqueda Lineal tuvo como objetivo analizar y diseñar algoritmos de búsqueda utilizando
estructuras secuenciales, con énfasis en modularidad, eficiencia y claridad del código. A través de cinco
ejercicios, se implementaron distintos tipos de búsqueda aplicadas a listas, diccionarios y sistemas
interactivos, empleando Python como lenguaje base.

Ejercicio 1 — Búsqueda Lineal Simple
Objetivo: Implementar la búsqueda secuencial en una lista de números.
Diseño: La función recorre la lista comparando cada elemento con el valor buscado.
Código resumido:
def busqueda_lineal_simple(lista, elemento): for i, x in enumerate(lista): if x == elemento: return i return -1
Ejemplo: lista = [64, 34, 25, 12, 22, 11, 90]; elemento = 25 → Retorna 2
Complejidad: O(n) en peor caso, O(1) en mejor caso, O(1) espacio adicional. 

Ejercicio 2 
Búsqueda en Productos
Objetivo: Aplicar búsqueda lineal en una lista de productos con atributos múltiples.
Diseño: Cada producto es un diccionario con claves: id, nombre, categoría y precio.
Código resumido:
def buscar_producto(lista, campo, valor): resultados = [] for producto in lista: if producto.get(campo) ==
valor: resultados.append(producto) return resultados Ejemplo: campo = "categoria", valor = "Periféricos"
→ Retorna productos con esa categoría.
Complejidad: O(n) tiempo y O(1) espacio adicional. 

Ejercicio 3
Búsqueda de Empleados
Objetivo: Desarrollar búsquedas por nombre completo, departamento y estado activo.
Diseño: Se usan comparaciones case-insensitive y filtros booleanos.
Código resumido:
def buscar_por_nombre_completo(lista, nombre, apellido): return [e for e in lista if
e['nombre'].lower()==nombre.lower() and e['apellido'].lower()==apellido.lower()] def
buscar_por_departamento(lista, depto): return [e for e in lista if e['departamento'].lower()==depto.lower()]
def buscar_activos(lista): return [e for e in lista if e['activo']] Ejemplo:
buscar_por_departamento(empleados, "Ventas") → retorna empleados del área de ventas.
Complejidad: O(n) tiempo, O(1) espacio adicional.

Ejercicio 4 — Búsqueda por Disponibilidad
Objetivo: Implementar filtros sobre una lista de productos según criterios específicos.
Diseño: Se agregaron cuatro funciones de filtrado: disponibilidad, rango de precios, marca y categoría.
Código resumido:
def productos_disponibles(lista): return [p for p in lista if p['stock'] > 0] def
productos_por_rango_precio(lista, minimo, maximo): return [p for p in lista if minimo <= p['precio'] <=
maximo] def productos_por_marca(lista, marca): return [p for p in lista if p['marca'].lower() ==
marca.lower()] def contar_por_categoria(lista, categoria): return sum(1 for p in lista if p['categoria'].lower()
== categoria.lower()) Ejemplo: productos_por_rango_precio(productos, 400, 1200) → devuelve artículos
en ese rango.
Complejidad: O(n) tiempo, O(1) espacio adicional.

Ejercicio 5 — Sistema Integrado con Menús
Objetivo: Integrar todas las funciones anteriores en un sistema completo con menús y submenús.
Diseño: Se creó un menú principal con tres secciones: productos, empleados y disponibilidad. Cada
opción ejecuta una de las funciones de búsqueda. Se implementaron validaciones de entrada y control de
errores mediante funciones auxiliares.
Características:
- Submenús interactivos.
- Validaciones de tipo numérico y texto.
- Impresión de resultados en consola.
- Opción de salida segura.
Complejidad: Cada búsqueda mantiene O(n) en tiempo, O(1) en espacio, y el sistema global O(n + k). 7.


Análisis Global
Los cinco ejercicios implementan el mismo principio de búsqueda secuencial o lineal. 
La complejidad global del
taller es O(n), siendo su eficiencia adecuada para pequeños conjuntos de datos. En casos de grandes
volúmenes de datos, se recomiendan algoritmos de búsqueda binaria o estructuras.
