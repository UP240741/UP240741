#Ejercicio 1
import random

def list_of_hexa_colors(n):
    colores = []
    for _ in range(n):
        hexa = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colores.append(hexa)
    return colores





#Ejercicio 2
def list_of_rgb_colors(n):
    colores = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores.append(f'rgb({r}, {g}, {b})')
    return colores




#Ejercicio 3
def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo de color no válido. Usa 'hexa' o 'rgb'."

