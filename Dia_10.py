#Level_1

#Ejercicio_1
for i in range(11):
    print(i)
i = 0
while i <= 10:
    print(i)
    i += 1

#Ejercicio_2
for i in range(10, -1, -1):
    print(i)
i = 10
while i >= 0:
    print(i)
    i -= 1


#Ejercicio_3
for i in range(1, 8):
    print('#' * i)

#Ejercicio_4
for _ in range(8):
    print('# ' * 8)

#Ejercicio_5
for i in range(11):
    print(f"{i} x {i} = {i * i}")


#Ejercicio_6
tech = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tech:
    print(item)

#Ejercicio_7
for i in range(0, 101, 2):
    print(i)


#Ejercicio_8
for i in range(1, 101, 2):
    print(i)


#Level_2

#Ejercicio_1
total = 0
for i in range(101):
    total += i
print("The sum of all numbers is", total)


#Ejercicio_2
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("The sum of all evens is", sum_even)
print("And the sum of all odds is", sum_odd)


#Level_3

#Ejercicio_1
countries = ['Finland', 'Ireland', 'Thailand', 'Canada', ...]
land_countries = [c for c in countries if 'land' in c]
print(land_countries)

#Ejercicio_2
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits[::-1]:
    reversed_fruits.append(fruit)
print(reversed_fruits)


#Ejercicio_3
countries_data = [
    {"name": "Finland", "languages": ["Finnish", "Swedish"]},
    {"name": "Switzerland", "languages": ["German", "French", "Italian"]},
    
]
all_langs = set()
for country in countries_data:
    all_langs.update(country.get('languages', []))
print("Total number of languages:", len(all_langs))

#Ejercicio_4
from collections import Counter
lang_counter = Counter()
for country in countries_data:
    lang_counter.update(country.get('languages', []))
most_common = lang_counter.most_common(10)
print("Top 10 most spoken languages:", most_common)


#Ejercicio_5
sorted_countries = sorted(countries_data, key=lambda x: x.get('population', 0), reverse=True)
top10 = sorted_countries[:10]
for country in top10:
    print(country['name'], country.get('population'))





