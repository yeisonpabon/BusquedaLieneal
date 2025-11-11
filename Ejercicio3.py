#Ejercicio 3 empleados 

empleados = [
    {"id": 101, "nombre": "Ana", "apellido": "Garcia", "departamento": "ventas", "salario":35000, "activo": True},
    {"id": 102, "nombre": "Luis", "apellido": "Martinez", "departamento": "marketing", "salario":40000, "activo": True},
    {"id": 103, "nombre": "Marta", "apellido": "Lopez", "departamento": "ventas", "salario":32000, "activo": False},
    {"id": 104, "nombre": "Carlos", "apellido": "Sanchez", "departamento": "IT", "salario":60000, "activo": True},
]

def buscar_por_nombre_completo(lista, nombre, apellido):

#complejidad O(n) peor caso y mejor caso O(1)

    n = nombre.strip().lower()
    a = apellido.strip().lower()
    resultados = []
    for e in lista :
        if e.get("nombre", "").strip().lower() == n and e.get("apellido", "").strip().lower() == a :
            resultados.append(e)
    return resultados
def buscar_por_departamento(lista, departamento):

    d = departamento.strip().lower()
    resultados = []
    for e in lista :
        if e.get("departamento", "").strip().lower() == d :
            resultados.append(e)
    return resultados
def buscar_por_activo(lista, activo):

    resultados = []
    for e in lista :
        if e.get("activo") == activo :
            resultados.append(e)
    return resultados

# Ejemplo de uso

print(buscar_por_nombre_completo(empleados, "Ana", "Garcia"))

print(buscar_por_departamento(empleados, "ventas"))

print(buscar_por_activo(empleados, True))

print(buscar_por_activo(empleados, False))

print(buscar_por_nombre_completo(empleados, "Luis", "Martinez"))

print(buscar_por_departamento(empleados, "IT"))