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


#Level_2

#Ejercicio_1
score = int(input("Enter the student's score (0-100): "))
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = None
if grade:
    print(f"Score: {score} - Grade: {grade}")
else:
    print("Invalid score. Please enter a value between 0 and 100.")


#Ejercicio_2
mes = input("Enter the month: ").strip().lower()
if mes in ['september', 'october', 'november']:
    estacion = 'Autumn'
elif mes in ['december', 'january', 'february']:
    estacion = 'Winter'
elif mes in ['march', 'april', 'may']:
    estacion = 'Spring'
elif mes in ['june', 'july', 'august']:
    estacion = 'Summer'
else:
    estacion = None
if estacion:
    print(f"The season is {estacion}.")
else:
    print("Invalid month entered.")

#Ejercicio_3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit name: ").strip().lower()
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print("Modified list:", fruits)


#Level_3

#Ejercicio_1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])
    if 'Python' in skills:
        print("Person has Python skill: True")
    else:
        print("Person has Python skill: False")
    skills_set = set(skills)
    if skills_set == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        if {'React', 'Node', 'MongoDB'}.issubset(skills_set):
            print("He is a fullstack developer")
        else:
            print("He is a backend developer")
    else:
        print("unknown title")
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")


