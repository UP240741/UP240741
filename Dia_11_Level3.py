# Level 3

#Ejercicio_1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
#Ejercicio_2
def are_items_unique(lst):
    return len(lst) == len(set(lst))

#Ejercicio_3
def are_same_type(lst):
    return all(type(x) == type(lst[0]) for x in lst)
#Ejercicio_4
def is_valid_variable(name):
    return name.isidentifier()