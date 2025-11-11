#busqueda en una lista de productos por su nombre

producto = {
    "id": int,
    "nombre" : str,
    "categoria": str,
    "precio": float
}

productos = [
    {"id": 1, "nombre": "Mouse",  "categoria": "Periféricos", "precio": 45.0},
    {"id": 2, "nombre": "Teclado","categoria": "Periféricos", "precio": 60.0},
    {"id": 3, "nombre": "Monitor","categoria": "Pantallas",   "precio": 550.0},
    {"id": 4, "nombre": "CPU",    "categoria": "Componentes", "precio": 850.0},
]

"""busca productos por un campo especifico usando busqueda lineal.
complejidad O(n) peor caso y mejor caso O(1)
"""
def buscar_prodcto(lista,campo, valor):

    resultados = []
    for producto in lista:
        if producto.get(campo) == valor:
            resultados.append(producto) 
    return resultados 

# Ejemplo de uso
print(buscar_prodcto(productos, "nombre", "Monitor"))

print(buscar_prodcto(productos, "categoria", "Periféricos"))

print(buscar_prodcto(productos, "id", 99))
