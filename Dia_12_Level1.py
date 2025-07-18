#Level_1


# Ejercicio_1
import random
import string
def random_user_id():
    caracteres = string.ascii_letters + string.digits  
    return ''.join(random.choice(caracteres) for _ in range(6))
print(random_user_id())  


#Ejercicio 2
def user_id_gen_by_user():
    num_caracteres = int(input("Ingrese el número de caracteres por ID: "))
    num_ids = int(input("Ingrese la cantidad de IDs a generar: "))

    caracteres = string.ascii_letters + string.digits
    ids = [''.join(random.choice(caracteres) for _ in range(num_caracteres)) for _ in range(num_ids)]

    for user_id in ids:
        print(user_id)

#Ejercicio 3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())  






