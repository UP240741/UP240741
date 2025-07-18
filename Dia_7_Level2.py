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
