#dia_3

edad=20
altura=1.72
num=complex(input("Ingrese un numero complejo: "))

base=float('Ingrese la base del triangulo: ')
altura=float("Ingrese la altura del triangulo: ")
area=0.5*base*altura
print('El area del triangulo es: ')

a= float(input('Ingrese lado a: '))
b= float(input('Ingrese lado b: '))
c= float(input('Ingrese lado c: '))
perimetro= a+b+c
print('El perimetro del triangulo es: ', perimetro)



longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

area = longitud * ancho
perimetro = 2 * (longitud + ancho)

print("El área del rectángulo es: {area}")
print("El perímetro del rectángulo es: {perimetro}")

print("Error: Por favor ingrese solo números válidos.")


pi = 3.14
radio = float(input("Ingrese el radio del círculo: "))
area = pi * radio * radio
circunferencia = 2 * pi * radio
print("El área del círculo es: {area}")
print("La circunferencia del círculo es: {circunferencia}")
print("Error: Por favor ingrese un número válido.")



m = 2      
b = -2     
x_y = 0
y_interseccion = m * x_y + b
x_interseccion = -b / m
y_x = 0
print("Ecuación de la recta: y = 2x - 2\n")
print("Pendiente (slope): {m}")
print(" Intersección con el eje Y: (0, {y_interseccion})")
print(" Intersección con el eje X: ({x_interseccion}, 0)")


import math
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Punto 1: (2, 2)")
print("Punto 2: (6, 10)\n")
print("Pendiente: {pendiente}")
print(" Distancia euclidiana: {distancia:.2f}")


pendiente_tarea_8 = 2
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente_tarea_9 = (y2 - y1) / (x2 - x1)
print("Tarea 8 - Ecuación: y = 2x - 2")
print("Pendiente = {pendiente_tarea_8}\n")

print("Tarea 8 - Ecuación: y = 2x - 2")
print("Pendiente = {pendiente_tarea_8}\n")

print("Tarea 9 - Puntos: (2, 2) y (6, 10)")
print("Pendiente calculada = {pendiente_tarea_9}\n")

if pendiente_tarea_8 == pendiente_tarea_9:
    print("Las pendientes son IGUALES. Las rectas son paralelas o coinciden.")
print("Las pendientes son DIFERENTES. Las rectas tienen distinta inclinación.")


def calcular_y(x):
    return x**2 + 6*x + 9

print("Calculando y = x^2 + 6x + 9 para valores de x del -10 al 10:\n")
for x in range(-10, 11):
    y = calcular_y(x)
    print(f"x = {x}, y = {y}")
    if y == 0:
        print(f"--> y es 0 cuando x = {x}\n")
print("Nota: La ecuación y = x^2 + 6x + 9 es un trinomio cuadrado perfecto (x + 3)^2, por lo que y = 0 solo cuando x = -3.")



palabra1 = "python"
palabra2 = "dragon"
longitud1 = len(palabra1)
longitud2 = len(palabra2)
print("Longitud de '{palabra1}': {longitud1}")
print("Longitud de '{palabra2}': {longitud2}")
comparacion = longitud1 > longitud2
print("¿La longitud de '{palabra1}' es mayor que la de '{palabra2}'? {comparacion} (Esto es una comparación falsa)")


palabra1 = "python"
palabra2 = "dragon"
do = ("on" in palabra1) and ("on" in palabra2)
print("¿'on' está en '{palabra1}' y en '{palabra2}'? {resultado}")


frase = "I hope this course is not full of jargon."
resultado = "jargon" in frase
print("¿La palabra 'jargon' está en la frase? {resultado}")


print("on" in "python")  
print("on" in "dragon") 
print(("on" in "python") and ("on" in "dragon")) 


texto = "python"
longitud = len(texto)
longitud_float = float(longitud)
longitud_str = str(longitud_float)
print("Longitud como entero: {longitud}")
print("Longitud convertida a float: {longitud_float}")
print("Longitud convertida a string: '{longitud_str}'")



numero = 8 
if numero % 2 == 0:
   print("El número {numero} es par.")
print("El número {numero} es impar.")


resultado_floor = 7 // 3
resultado_int = int(2.7)
comparacion = resultado_floor == resultado_int
print("7 // 3 = {resultado_floor}")
print("int(2.7) = {resultado_int}")
print("¿Son iguales? {comparacion}")


tipo_str = type('10')
tipo_int = type(10)
comparacion = tipo_str == tipo_int
print("Tipo de '10': {tipo_str}")
print("Tipo de 10: {tipo_int}")
print("¿Son iguales los tipos? {comparacion}")


numero_str = '9.8'
numero_float = float(numero_str) 
numero_int = int(numero_float)    
comparacion = numero_int == 10
print("int(float('{numero_str}')) = {numero_int}")
print("¿Es igual a 10? {comparacion}")



horas = float(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
pago = horas * tarifa
print("Su ganancia semanal es {pago}")



años = int(input("Ingrese el número de años que ha vivido: "))
segundos_por_año = 365 * 24 * 60 * 60
segundos_vividos = años * segundos_por_año
print("Has vivido {segundos_vividos} segundos.")



for i in range(1, 6):
   print(i, 1, i, i**2, i**3)


