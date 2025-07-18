#Level_3

#Ejercicio_1
ages = [22, 35, 22, 40, 35, 50]
ages_set = set(ages)
len_list = len(ages)
len_set = len(ages_set)
print("Longitud de la lista:", len_list)
print("Longitud del set:", len_set)
if len_list > len_set:
    print("La lista es más grande porque contiene duplicados.")
elif len_list < len_set:
    print("El set es más grande (esto sería raro).")
else:
    print("La lista y el set tienen la misma cantidad de elementos.")


#Ejercicio_2
s = "Hola"
print(s[0])  
lista = [1, 2, 3, "a", "b"]
lista[0] = 10  
lista.append(4)
tupla = (1, 2, 3)
conjunto = {1, 2, 3, 3}
print(conjunto)  
conjunto.add(4) 

#Ejercicio_3
sentence = "I am a teacher and I love to inspire and teach people."
sentence = sentence.replace('.', '')
words = sentence.split()
unique_words = set(words)
num_unique_words = len(unique_words)
print("Palabras únicas:", unique_words)
print("Número de palabras únicas:", num_unique_words)



