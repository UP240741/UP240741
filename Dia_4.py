#1
resultado = '30' + ' ' + 'dias' + ' ' + 'de' + ' ' + 'Python'
print(resultado)
resultado2 = ' '.join(['30', 'Dias', 'de', 'Python'])
print(resultado2)

#2
resultado = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(resultado)
resultado2 = ' '.join(['Coding', 'For', 'All'])
print(resultado2)

#3
company = "Coding For All"
print(company)

#4
company = "Coding For All"
print(company)

#5
company = "Coding For All"
print(len(company))

#6
company = "Coding For All"
print(company.upper())

#7
company = "Coding For All"
print(company.lower())

#8
company = "Coding For All"
print("capitalize():", company.capitalize())
print("titulo():", company.titulo())
print("swapcase():", company.swapcase())

#9
company = "Coding For All"
primera_palabra = company[0:6]  
print(primera_palabra)

#10
company = "Coding For All"
pos = company.find("Coding")
if pos != -1:
    print(f"La palabra 'Coding' se encontró en la posición {pos}")
else:
    print("La palabra 'Coding' no se encontró")
try:
    pos = company.index("Coding")
    print(f"La palabra 'Coding' se encontró en la posición {pos}")
except ValueError:
    print("La palabra 'Coding' no se encontró")
if "Coding" in company:
    print("La palabra 'Coding' está en la cadena")
else:
    print("La palabra 'Coding' no está en la cadena")

#11
company = "Coding For All"
nuevo_string = company.replace("Coding", "Python")
print(nuevo_string)

#12
texto = "Python for Everyone"
nuevo_texto = texto.replace("Everyone", "All")
print(nuevo_texto)

#13
company = "Coding For All"
palabras = company.split(' ')
print(palabras)

#14
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
lista_empresas = empresas.split(',')
print(lista_empresas)

#15
company = "Coding For All"
print(company[0])

#16
company = "Coding For All"
ultimo_indice = len(company) - 1
print(ultimo_indice)

#17
company = "Coding For All"
print(company[10])

#18
nombre = "Python For Everyone"
palabras = nombre.split()
acronimo = ''.join(p[0].upper() for p in palabras)
print(acronimo)

#19
nombre = "Coding For All"
palabras = nombre.split()
acronimo = ''.join(p[0].upper() for p in palabras)
print(acronimo)

#20
company = "Coding For All"
posicion = company.index('C')
print(posicion)

#21
company = "Coding For All"
posicion = company.index('F')
print(posicion)

#22
company = "Coding For All People"
posicion = company.rfind('l')
print(posicion)

#23
frase = "You cannot end a sentence with because because because is a conjunction"
pos_find = frase.find("because")
print("Usando find():", pos_find)
pos_index = frase.index("because")
print("Usando index():", pos_index)

#24
frase = "You cannot end a sentence with because because because is a conjunction"
pos_ultima = frase.rindex("because")
print(pos_ultima)

#25
frase = "You cannot end a sentence with because because because is a conjunction"
inicio = frase.find("because because because")
longitud = len("because because because")
frase_cortada = frase[inicio:inicio+longitud]
print(frase_cortada)

#26
frase = "You cannot end a sentence with because because because is a conjunction"
posicion = frase.find("because")
print(posicion)

#27
frase = "You cannot end a sentence with because because because is a conjunction"
inicio = frase.find("because because because")
longitud = len("because because because")
frase_cortada = frase[inicio:inicio + longitud]
print(frase_cortada)

#28
company = "Coding For All"
resultado = company.startswith("Coding")
print(resultado)

#29
company = "Coding For All"
resultado = company.endswith("coding")
print(resultado)

#30
texto = '   Coding For All      '
texto_limpio = texto.strip()
print(f"Antes: '{texto}'")
print(f"Después: '{texto_limpio}'")

#31
print("30DaysOfPython".isidentifier())        
print("thirty_days_of_python".isidentifier()) 

#32
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = '# '.join(librerias)
print(resultado)

#33
frases = "I am enjoying this challenge.\nI just wonder what is next."
print(frases)

#34
texto = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(texto)

#35
radio = 10
area = 3.14 * radio ** 2
mensaje = "El area del circulo con radio {} en {} metros cuadrados.".format(radio, area)
print(mensaje)

#36
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))  
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))


