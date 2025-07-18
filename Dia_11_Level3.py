# Level 3

import math

# Ejercicio 1: 
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Ejercicio 2: 
def elementos_unicos(lista):
    return len(lista) == len(set(lista))

# Ejercicio 3:
def mismo_tipo(lista):
    return all(type(x) == type(lista[0]) for x in lista)

# Ejercicio 4: 
def es_variable_valida(nombre):
    return nombre.isidentifier()
