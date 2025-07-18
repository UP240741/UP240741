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


