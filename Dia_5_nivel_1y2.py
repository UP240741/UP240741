#Level_1

#1
mi_lista = []

#2
mi_lista = [10, 20, 30, 40, 50, 60]

#3
mi_lista = [10, 20, 30, 40, 50, 60]
longitud = len(mi_lista)
print("La longitud de la lista es:", longitud)

#4
mi_lista = [10, 20, 30, 40, 50, 60, 70]
primer_elemento = mi_lista[0]
indice_medio = len(mi_lista) // 2
elemento_medio = mi_lista[indice_medio]
ultimo_elemento = mi_lista[-1]
print("Primer elemento:", primer_elemento)
print("Elemento del medio:", elemento_medio)
print("Último elemento:", ultimo_elemento)

#5
mixed_data_types = ["Alondra", 20, 1.75, "casada", "Rinconada"]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
mi_lista = [10, 20, 30, 40, 50]
print("Contenido de la lista:")
print(mi_lista)

#8
empresas = ["Apple", "Google", "Microsoft", "Amazon", "Meta"]
print("Número de empresas en la lista:", len(empresas))

#9
empresas = ["Apple", "Google", "Microsoft", "Amazon", "Meta"]
primera = empresas[0]
medio = empresas[len(empresas) // 2]
ultima = empresas[-1]
print("Primera empresa:", primera)
print("Empresa del medio:", medio)
print("Última empresa:", ultima)


#10
empresas = ["Apple", "Google", "Microsoft", "Amazon", "Meta"]
empresas[1] = "Apple"
print("Lista de empresas modificada:")
print(empresas)

#11
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta"]
it_companies.append("Apple")
print("Lista de empresas IT actualizada:")
print(it_companies)

#12
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta"]
nueva_empresa = "Apple"
indice_medio = len(it_companies) // 2
it_companies.insert(indice_medio, nueva_empresa)
print("Lista de empresas IT con nueva empresa en el medio:")
print(it_companies)


#13
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
        break  
print("Lista con una empresa en mayúsculas (excepto IBM):")
print(it_companies)


#14
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
resultado = '#;  '.join(it_companies)
print("Lista unida con '#;  ' como separador:")
print(resultado)


#15
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
empresa_a_buscar = "Google"
if empresa_a_buscar in it_companies:
    print(f"La empresa '{empresa_a_buscar}' está en la lista.")
else:
    print(f"La empresa '{empresa_a_buscar}' NO está en la lista.")


#16
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
it_companies.sort()
print("Lista de empresas IT ordenada:")
print(it_companies)


#17
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
it_companies.sort()
it_companies.reverse()
print("Lista de empresas IT en orden descendente:")
print(it_companies)

#18
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
primeras_tres = it_companies[:3]
print("Las primeras 3 empresas son:")
print(primeras_tres)

#19
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
ultimas_tres = it_companies[-3:]
print("Las últimas 3 empresas son:")
print(ultimas_tres)

#20
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
n = len(it_companies)
if n % 2 == 1:

    indice_medio = n // 2
    empresas_medio = it_companies[indice_medio:indice_medio+1]
else:
    
    indice_medio1 = n//2 - 1
    indice_medio2 = n//2
    empresas_medio = it_companies[indice_medio1:indice_medio2+1]
print("Empresa(s) del medio:")
print(empresas_medio)

#21
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
primera_eliminada = it_companies.pop(0)
print("Empresa eliminada:", primera_eliminada)
print("Lista después de eliminar la primera empresa:")
print(it_companies)

it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
del it_companies[0]
print("Lista después de eliminar la primera empresa:")
print(it_companies)

#22
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
n = len(it_companies)
if n % 2 == 1:
    indice_medio = n // 2
    empresa_eliminada = it_companies.pop(indice_medio)
    print(f"Empresa eliminada del medio: {empresa_eliminada}")
else:
    indice_medio1 = n // 2 - 1
    indice_medio2 = n // 2
    empresas_eliminadas = it_companies[indice_medio1:indice_medio2+1]
    del it_companies[indice_medio1:indice_medio2+1]
    print(f"Empresas eliminadas del medio: {empresas_eliminadas}")
print("Lista actualizada:")
print(it_companies)


#23
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
ultima_eliminada = it_companies.pop()
print("Empresa eliminada:", ultima_eliminada)
print("Lista después de eliminar la última empresa:")
print(it_companies)

it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
del it_companies[-1]
print("Lista después de eliminar la última empresa:")
print(it_companies)

#24
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
it_companies.clear()
print("Lista después de eliminar todas las empresas:")
print(it_companies)

#25
it_companies = ["Apple", "Google", "Microsoft", "Amazon", "Meta", "IBM"]
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print("Lista unida (full_stack):")
print(full_stack)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print("Lista front_end después de extender:")
print(front_end)


#27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
full_stack = joined_list.copy()
indice_redux = full_stack.index('Redux')
full_stack.insert(indice_redux + 1, 'Python')
full_stack.insert(indice_redux + 2, 'SQL')
print("Lista full_stack actualizada:")
print(full_stack)



#Level_2

#1
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()

edad_minima = edades[0]
edad_maxima = edades[-1]

edades.append(edad_minima)
edades.append(edad_maxima)

edades.sort()

n = len(edades)
if n % 2 == 1:
    mediana = edades[n // 2]
else:
    mediana = (edades[n//2 - 1] + edades[n//2]) / 2

promedio = sum(edades) / n

rango = edad_maxima - edad_minima

abs_min = abs(edad_minima - promedio)
abs_max = abs(edad_maxima - promedio)

print("Lista ordenada con min y max agregados:")
print(edades)
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")
print(f"Mediana: {mediana}")
print(f"Promedio: {promedio:.2f}")
print(f"Rango: {rango}")
print(f"Valor absoluto de (min - promedio): {abs_min:.2f}")
print(f"Valor absoluto de (max - promedio): {abs_max:.2f}")


#1
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria']
n = len(countries)

if n % 2 == 1:
    indice_medio = n // 2
    paises_medio = countries[indice_medio:indice_medio+1]
else:
    indice_medio1 = n // 2 - 1
    indice_medio2 = n // 2
    paises_medio = countries[indice_medio1:indice_medio2+1]
print("País(es) del medio:")
print(paises_medio)


#2
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria']
n = len(countries)

if n % 2 == 0:
    mitad = n // 2
else:
    mitad = n // 2 + 1
primera_mitad = countries[:mitad]
segunda_mitad = countries[mitad:]
print("Primera mitad:")
print(primera_mitad)
print("Segunda mitad:")
print(segunda_mitad)


#3
ciudades = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

primera_ciudad, segunda_ciudad, tercera_ciudad, *escandinavos_ciudades = ciudades

print("Primer país:", primera_ciudad)
print("Segundo país:", segunda_ciudad)
print("Tercer país:", tercera_ciudad)
print("Países escandinavos:", escandinavos_ciudades)
