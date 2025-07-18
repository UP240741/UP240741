#Level_1

#Ejercicio_1
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres lo suficientemente mayor para aprender a conducir.")
else:
    años_faltantes = 18 - edad
    print(f"Necesitas {años_faltantes} años más para aprender a conducir.")

#Ejercicio_2
my_age = 25
your_age = int(input("Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")
else:
    print("We are the same age.")


#Ejercicio_3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


