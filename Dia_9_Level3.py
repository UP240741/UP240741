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


