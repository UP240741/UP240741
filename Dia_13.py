#Ejercicio_1
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numeros if n <= 0]
print(negativos_y_ceros)  # [-4, -3, -2, -1, 0]


#Ejercicio_2
lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplanada = [num for sublista in lista_de_listas for interna in sublista for num in interna]
print(aplanada)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


#Ejercicio_3
tabla = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
print(tabla)


#Ejercicio_4
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
paises_convertidos = [[pais.upper(), pais[:3].upper(), ciudad.upper()] 
                      for par in paises for (pais, ciudad) in par]
print(paises_convertidos)


#Ejercicio_5
diccionarios = [{'pais': pais.upper(), 'ciudad': ciudad.upper()} 
                for par in paises for (pais, ciudad) in par]
print(diccionarios)


#Ejercicio_6
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [f"{nombre} {apellido}" for par in nombres for (nombre, apellido) in par]
print(nombres_completos)


#Ejercicio_7
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'Indefinida'
print(pendiente(2, 3, 4, 7))  # 2.0


