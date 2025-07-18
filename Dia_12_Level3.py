#Ejercicio 1
import random

def shuffle_list(lista):
    lista_mezclada = lista[:]  
    random.shuffle(lista_mezclada)
    return lista_mezclada



#Ejercicio 2
def unique_random_numbers():
    return random.sample(range(10), 7) 

