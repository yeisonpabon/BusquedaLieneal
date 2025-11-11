#busqueda por disponibilidad 


productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple',   'categoria': 'Smartphone', 'precio': 999.99,  'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99,  'stock': 8,  'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple',   'categoria': 'Laptop',     'precio': 1299.99, 'stock': 5,  'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13',   'marca': 'Dell',    'categoria': 'Laptop',     'precio': 1199.99, 'stock': 0,  'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony',   'categoria': 'Audífonos',  'precio': 399.99,  'stock': 15, 'disponible': True}
]

def productos_disponibles(lista):
    """
    Complejidad: O(n) tiempo, O(1) espacio adicional (sin contar la salida).
    """
    return [p for p in lista if p.get('stock', 0) > 0]

def productos_por_rango_precio(lista, minimo, maximo, incluir_bordes=True):
    """
    Complejidad: O(n) tiempo.
    """
    if incluir_bordes:
        return [p for p in lista if minimo <= p.get('precio', 0.0) <= maximo]
    else:
        return [p for p in lista if minimo < p.get('precio', 0.0) < maximo]

def productos_por_marca(lista, marca):
    """
    Complejidad: O(n) tiempo.
    """
    m = str(marca).strip().lower()
    return [p for p in lista if str(p.get('marca', '')).strip().lower() == m]

def contar_por_categoria(lista, categoria):
    """
    Complejidad: O(n) tiempo.
    """
    c = str(categoria).strip().lower()
    return sum(1 for p in lista if str(p.get('categoria', '')).strip().lower() == c)


if __name__ == "__main__":
    print("== 1) Disponibles (stock > 0) ==")
    print(productos_disponibles(productos))  # Espera: todos excepto el id=4

    print("\n== 2) Rango de precios ==")
    print(productos_por_rango_precio(productos, 400, 1200))      # Espera: ids 2,4,5
    print(productos_por_rango_precio(productos, 900, 1000))      # Espera: id 1
    print(productos_por_rango_precio(productos, 900, 1000, False))  # Espera: []

    print("\n== 3) Marca específica ==")
    print(productos_por_marca(productos, "Apple"))   # Espera: ids 1 y 3
    print(productos_por_marca(productos, "sony"))    # Espera: id 5

    print("\n== 4) Contar por categoría ==")
    print(contar_por_categoria(productos, "Laptop"))      # Espera: 2
    print(contar_por_categoria(productos, "Smartphone"))  # Espera: 2
