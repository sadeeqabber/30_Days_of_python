# Day 6: 30 Days of python programming

# 1: empty dictionary called dog
dog = {}

# 2: add name, color, breed, legs, age (key = value pairs)
dog['name'] = 'Rex'
dog['color'] = 'brown'
dog['breed'] = 'German Shepherd'
dog['legs'] = 4
dog['age'] = 3
print(dog)

# 3: student dictionary
student = {
    'first_name': 'Amina',
    'last_name': 'Bello',
    'gender': 'female',
    'age': 25,
    'marital_status': 'single',
    'skills': ['Python', 'Excel', 'SQL'],
    'country': 'Nigeria',
    'city': 'Kano',
    'address': {
        'street': 'Zoo Road',
        'zipcode': '700001'
    }
}

# 4: number of key: value pairs
print(len(student))

# 5: value of skills and its type
print(student['skills'])
print(type(student['skills']))

# 6: add skills
student['skills'].append('Power BI')
student['skills'].append('Statistics')
print(student['skills'])

# 7: keys
print(list(student.keys()))

# 8: values
print(list(student.values()))

# 9: list of tuples
print(list(student.items()))

# 10: delete one item
student.pop('marital_status')
print(student)

# 11: delete one of the dictionaries
del dog
# print(dog)   