#Level_1


# Ejercicio_1
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

#Ejercicio_2
def user_id_gen_by_user():
    length = int(input("Enter the number of characters per ID: "))
    count = int(input("Enter the number of IDs to generate: "))
    for _ in range(count):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=length)))

#Ejercicio_3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


#Level_2

#Ejercicio_1
def list_of_hexa_colors(count):
    colors = []
    for _ in range(count):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(hex_color)
    return colors

#Ejercicio_2
def list_of_rgb_colors(count):
    return [rgb_color_gen() for _ in range(count)]

#Ejercicio_3
def generate_colors(type_, count):
    if type_.lower() == 'hexa':
        return list_of_hexa_colors(count)
    elif type_.lower() == 'rgb':
        return list_of_rgb_colors(count)
    else:
        return "Unsupported color type"


#Level_3

#Ejercicio_1
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

#Ejercicio_2
def unique_random_numbers():
    return random.sample(range(10), 7)




