# Level 2

import math
from statistics import mean, median, variance, stdev
from collections import Counter

# Ejercicio 1:
def contar_pares_e_impares(n):
    pares = sum(1 for i in range(n + 1) if i % 2 == 0)
    impares = n + 1 - pares
    return f"Cantidad de impares: {impares}. Cantidad de pares: {pares}."

# Ejercicio 2:
def factorial(n):
    return math.factorial(n)

# Ejercicio 3: 
def esta_vacio(parametro):
    return not bool(parametro)

# Ejercicio 4: 
def calcular_media(lista):
    return mean(lista)

def calcular_mediana(lista):
    return median(lista)

def calcular_moda(lista):
    return Counter(lista).most_common(1)[0][0]

def calcular_rango(lista):
    return max(lista) - min(lista)

def calcular_varianza(lista):
    return variance(lista)

def calcular_desviacion_estandar(lista):
    return stdev(lista)


