#dia_8

#Ejercicio_1
dog = {}

#ejercicio_2
dog['name'] = 'Firulais'
dog['color'] = 'marrón'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

#Ejercicio_3
student = {
    'first_name': 'Ana',
    'last_name': 'García',
    'gender': 'Femenino',
    'age': 22,
    'marital_status': 'Soltera',
    'skills': ['Python', 'Data Analysis'],
    'country': 'España',
    'city': 'Madrid',
    'address': 'Calle Falsa 123'
}


#Ejercicio_4
longitud = len(student)
print("Número de pares clave-valor en student:", longitud)


#Ejercicio_5
skills = student.get('skills')
print("Skills:", skills)
print("Tipo de dato de skills:", type(skills))


#Ejercicio_6
student['skills'].append('Machine Learning')
student['skills'].append('Comunicación')
print("Skills actualizadas:", student['skills'])


#Ejercicio_7
keys_list = list(student.keys())
print("Claves:", keys_list)


#Ejercicio_8
values_list = list(student.values())
print("Valores:", values_list)


#Ejercicio_9
items_list = list(student.items())
print("Lista de tuplas (items):", items_list)


#Ejercicio_10
del student['marital_status']
print("Diccionario después de eliminar marital_status:", student)


#Ejercicio_11
del dog


