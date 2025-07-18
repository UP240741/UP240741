

# Level 1

import math

# Ejercicio 1:
def sumar_dos_numeros(a, b):
    return a + b

# Ejercicio 2: 
def area_circulo(radio):
    return math.pi * radio * radio

# Ejercicio 3: 
def sumar_todos_los_numeros(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    return "Todos los argumentos deben ser números"

# Ejercicio 4: 
def convertir_celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

# Ejercicio 5: 
def comprobar_estacion(mes):
    mes = mes.lower()
    if mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    elif mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    else:
        return 'Mes inválido'

# Ejercicio 6: 
def calcular_pendiente(x1, y1, x2, y2):
    if x2 == x1:
        return "Pendiente indefinida (línea vertical)"
    return (y2 - y1) / (x2 - x1)

# Ejercicio 7: 
def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    if discriminante < 0:
        return "No tiene raíces reales"
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return (raiz,)
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (raiz1, raiz2)

# Ejercicio 8: 
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

# Ejercicio 9: 
def invertir_lista(lista):
    return lista[::-1]

# Ejercicio 10: 
def capitalizar_elementos_lista(lista):
    return [elemento.capitalize() for elemento in lista]

# Ejercicio 11: 
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

# Ejercicio 12: 
def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

# Ejercicio 13: 
def suma_numeros(n):
    return sum(range(n + 1))

# Ejercicio 14: 
def suma_impares(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# Ejercicio 15: 
def suma_pares(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)




