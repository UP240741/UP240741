#Dia_7

#Level_1

#Ejercicio_1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
cantidad = len(it_companies)
print("Número de empresas IT:", cantidad)

#Ejercicio_2
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print(it_companies)

#Ejercicio_3
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.update(['Twitter', 'Snapchat', 'Netflix'])
print(it_companies)

#Ejercicio_4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.remove('IBM')
print(it_companies)

#Ejercicio_5
conjunto = {'a', 'b', 'c'}
conjunto.remove('b') 
conjunto.discard('d')  
conjunto.remove('d')  

#Level_2

#Ejercicio_1
A = [1, 2, 3]
B = [4, 5, 6]
resultado = A + B
print(resultado)  # [1, 2, 3, 4, 5, 6]

#Ejercicio_2
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
interseccion = A.intersection(B)
print(interseccion)  
interseccion2 = A & B
print(interseccion2)  

#Ejercicio_3
A = {1, 2}
B = {1, 2, 3, 4}
es_subconjunto = A.issubset(B)
print(es_subconjunto)  
es_subconjunto2 = A <= B
print(es_subconjunto2)  

#Ejercicio_4
A = {1, 2, 3}
B = {4, 5, 6}
son_disjuntos = A.isdisjoint(B)
print(son_disjuntos)  

#Ejercicio_5
A = {1, 2, 3}
B = {4, 5, 6}
union_A_B = A.union(B)
print("A unido con B:", union_A_B)
union_B_A = B.union(A)
print("B unido con A:", union_B_A)

#Ejercicio_6
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
diff_simetrica = A.symmetric_difference(B)
print(diff_simetrica)  
diff_simetrica2 = A ^ B
print(diff_simetrica2)  

#Ejercicio_7
A = {1, 2, 3}
B = {4, 5, 6}
del A
del B


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
# Frase
sentence = "I am a teacher and I love to inspire and teach people."
sentence = sentence.replace('.', '')
words = sentence.split()
unique_words = set(words)
num_unique_words = len(unique_words)
print("Palabras únicas:", unique_words)
print("Número de palabras únicas:", num_unique_words)










