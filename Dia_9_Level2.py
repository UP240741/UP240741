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
