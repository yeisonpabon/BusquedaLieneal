#menu interactivo

# Sistema integrado para búsquedas con menús y validaciones

from typing import List, Dict, Any

# Datos de ejemplo (del taller)

productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple',   'categoria': 'Smartphone', 'precio': 999.99,  'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99,  'stock': 8,  'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple',   'categoria': 'Laptop',     'precio': 1299.99, 'stock': 5,  'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13',   'marca': 'Dell',    'categoria': 'Laptop',     'precio': 1199.99, 'stock': 0,  'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony',   'categoria': 'Audífonos',  'precio': 399.99,  'stock': 15, 'disponible': True}
]

empleados = [
    {'id': 101, 'nombre': 'Ana',    'apellido': 'García',    'departamento': 'Ventas',     'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López',     'departamento': 'Técnico',    'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María',  'apellido': 'Rodríguez', 'departamento': 'Ventas',     'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José',   'apellido': 'Martínez',  'departamento': 'Inventario', 'salario': 30000, 'activo': True}
]
# Utilidades

def input_int(mensaje: str) -> int:
    while True:
        s = input(mensaje).strip()
        try:
            return int(s)
        except ValueError:
            print("Entrada inválida: debe ser un número entero.")

def input_float(mensaje: str) -> float:
    while True:
        s = input(mensaje).strip()
        try:
            return float(s)
        except ValueError:
            print("Entrada inválida: debe ser un número (usa punto decimal).")

def input_str_no_vacio(mensaje: str) -> str:
    while True:
        s = input(mensaje).strip()
        if s:
            return s
        print("Entrada vacía: escribe algún valor.")

def mostrar_lista(tabla: List[Dict[str, Any]]) -> None:
    if not tabla:
        print("Sin resultados.")
        return
    for fila in tabla:
        print(fila)

# Búsquedas sobre productos

def buscar_producto_por_nombre(lista, nombre):
    n = nombre.strip().lower()
    return [p for p in lista if str(p.get('nombre', '')).strip().lower() == n]

def buscar_producto_por_id(lista, id_val):
    return [p for p in lista if p.get('id') == id_val]

def buscar_producto_por_categoria(lista, categoria):
    c = categoria.strip().lower()
    return [p for p in lista if str(p.get('categoria', '')).strip().lower() == c]

def productos_disponibles(lista):
    return [p for p in lista if p.get('stock', 0) > 0]

def productos_por_rango_precio(lista, minimo, maximo, incluir_bordes=True):
    if incluir_bordes:
        return [p for p in lista if minimo <= p.get('precio', 0.0) <= maximo]
    else:
        return [p for p in lista if minimo < p.get('precio', 0.0) < maximo]

def productos_por_marca(lista, marca):
    m = marca.strip().lower()
    return [p for p in lista if str(p.get('marca', '')).strip().lower() == m]

def contar_por_categoria(lista, categoria):
    c = categoria.strip().lower()
    return sum(1 for p in lista if str(p.get('categoria', '')).strip().lower() == c)

# Búsquedas sobre empleados 

def buscar_empleado_por_nombre_completo(lista, nombre, apellido):
    n = nombre.strip().lower()
    a = apellido.strip().lower()
    return [e for e in lista if str(e.get('nombre','')).strip().lower()==n and str(e.get('apellido','')).strip().lower()==a]

def buscar_empleado_por_departamento(lista, depto):
    d = depto.strip().lower()
    return [e for e in lista if str(e.get('departamento','')).strip().lower()==d]

def buscar_empleados_activos(lista):
    return [e for e in lista if e.get('activo') is True]

# Submenús
def submenu_productos():
    while True:
        print("\n--- Submenú Productos ---")
        print("1) Buscar por nombre")
        print("2) Buscar por ID")
        print("3) Buscar por categoría")
        print("4) Volver")
        opcion = input_str_no_vacio("Opción: ")
        if opcion == "1":
            nombre = input_str_no_vacio("Nombre exacto: ")
            mostrar_lista(buscar_producto_por_nombre(productos, nombre))
        elif opcion == "2":
            id_val = input_int("ID (entero): ")
            mostrar_lista(buscar_producto_por_id(productos, id_val))
        elif opcion == "3":
            cat = input_str_no_vacio("Categoría: ")
            mostrar_lista(buscar_producto_por_categoria(productos, cat))
        elif opcion == "4":
            return
        else:
            print("Opción no válida.")

def submenu_empleados():
    while True:
        print("\n--- Submenú Empleados ---")
        print("1) Buscar por nombre completo")
        print("2) Buscar por departamento")
        print("3) Listar activos")
        print("4) Volver")
        opcion = input_str_no_vacio("Opción: ")
        if opcion == "1":
            nom = input_str_no_vacio("Nombre: ")
            ape = input_str_no_vacio("Apellido: ")
            mostrar_lista(buscar_empleado_por_nombre_completo(empleados, nom, ape))
        elif opcion == "2":
            depto = input_str_no_vacio("Departamento: ")
            mostrar_lista(buscar_empleado_por_departamento(empleados, depto))
        elif opcion == "3":
            mostrar_lista(buscar_empleados_activos(empleados))
        elif opcion == "4":
            return
        else:
            print("Opción no válida.")

def submenu_disponibilidad():
    while True:
        print("\n--- Submenú Disponibilidad ---")
        print("1) Productos disponibles (stock > 0)")
        print("2) Productos por rango de precios")
        print("3) Productos por marca")
        print("4) Contar productos por categoría")
        print("5) Volver")
        opcion = input_str_no_vacio("Opción: ")
        if opcion == "1":
            mostrar_lista(productos_disponibles(productos))
        elif opcion == "2":
            minimo = input_float("Precio mínimo: ")
            maximo = input_float("Precio máximo: ")
            if maximo < minimo:
                print("Rango inválido: el máximo no puede ser menor que el mínimo.")
                continue
            incluir = input_str_no_vacio("¿Incluir bordes? (s/n): ").lower().startswith("s")
            mostrar_lista(productos_por_rango_precio(productos, minimo, maximo, incluir))
        elif opcion == "3":
            marca = input_str_no_vacio("Marca: ")
            mostrar_lista(productos_por_marca(productos, marca))
        elif opcion == "4":
            cat = input_str_no_vacio("Categoría: ")
            print(f"Total en '{cat}': {contar_por_categoria(productos, cat)}")
        elif opcion == "5":
            return
        else:
            print("Opción no válida.")

# Menú principal

def menu_principal():
    while True:
        print("\n=== SISTEMA DE BÚSQUEDAS ===")
        print("1) Búsquedas en productos")
        print("2) Búsquedas en empleados")
        print("3) Búsquedas de disponibilidad")
        print("0) Salir")
        op = input_str_no_vacio("Opción: ")
        if op == "1":
            submenu_productos()
        elif op == "2":
            submenu_empleados()
        elif op == "3":
            submenu_disponibilidad()
        elif op == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
