def busqueda_lineal_simple(lista, elemento):
 """busca un elemento en una lista usando busqueda lineal 
 complejidad O(n) peor caso y mejor caso O(1)"""

 for i, x in enumerate(lista):
  if x == elemento:
    return i
 return -1

# Ejemplo de uso
numeros = [4, 2, 5, 1, 3]
print(busqueda_lineal_simple(numeros, 1))  # Salida: 3
print(busqueda_lineal_simple(numeros, 6))  # Salida: -