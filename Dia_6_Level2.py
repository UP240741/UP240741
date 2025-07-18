#Level_2

#Ejercicio_1
family_members = ('Lucía', 'María', 'Sofía', 'Carlos', 'Andrés', 'Javier', 'Juan', 'Ana')
siblings = family_members[:6]
parents = family_members[6:]
print("Hermanos y hermanas:", siblings)
print("Padres:", parents)

#Ejercicio_2
frutas = ("manzana", "banana", "naranja")
verduras = ("zanahoria", "lechuga", "brócoli")
productos_animales = ("leche", "queso", "huevo")
food_stuff_tp = frutas + verduras + productos_animales
print(food_stuff_tp)

#Ejercicio_3
food_stuff_tp = ('manzana', 'banana', 'naranja', 'zanahoria', 'lechuga', 'brócoli', 'leche', 'queso', 'huevo')
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Ejercicio_4
food_stuff_tp = ('manzana', 'banana', 'naranja', 'zanahoria', 'lechuga', 'brócoli', 'leche', 'queso', 'huevo')
food_stuff_lt = list(food_stuff_tp)
n = len(food_stuff_lt)
if n % 2 != 0:
    mid_index = n // 2
    middle_items = food_stuff_lt[mid_index:mid_index+1]
else:
    mid_index1 = n // 2 - 1
    mid_index2 = n // 2
    middle_items = food_stuff_lt[mid_index1:mid_index2+1]
print("Elemento(s) del medio:", middle_items)

#Ejercicio_5
food_stuff_lt = ['manzana', 'banana', 'naranja', 'zanahoria', 'lechuga', 'brócoli', 'leche', 'queso', 'huevo']
primeros_tres = food_stuff_lt[:3]
ultimos_tres = food_stuff_lt[-3:]
print("Primeros tres:", primeros_tres)
print("Últimos tres:", ultimos_tres)

#Ejercicico_6
del food_stuff_tp

#Ejercicio_7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  
print('Iceland' in nordic_countries) 


