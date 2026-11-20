# Day 7: 30 Days of python programming

# ---------------- Level 1 ----------------

# 1: driving age (input() gives text, so convert with int())
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    missing = 18 - age
    print(f'You need {missing} more years to learn to drive.')

# 2: compare ages (my_age is a fixed value)
my_age = 25
your_age = int(input('Enter your age: '))
if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:                     # nested condition: 'year' vs 'years'
        print('You are 1 year older than me.')
    else:
        print(f'You are {difference} years older than me.')
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print('You are 1 year younger than me.')
    else:
        print(f'You are {difference} years younger than me.')
else:
    print('We are the same age.')

# 3: compare two numbers
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

# ---------------- Level 2 ----------------

# 1: grades (the ranges in the exercise overlap at 80-89, so I used A: 80-100, B: 70-79)
score = float(input('Enter the score: '))
if score > 100 or score < 0:
    print('Invalid score')
elif score >= 80:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
elif score >= 50:
    print('D')
else:
    print('F')

# 2: season (.title() makes 'march' or 'MARCH' become 'March')
month = input('Enter the month: ').title()
if month in ['September', 'October', 'November']:
    print('The season is Autumn')
elif month in ['December', 'January', 'February']:
    print('The season is Winter')
elif month in ['March', 'April', 'May']:
    print('The season is Spring')
elif month in ['June', 'July', 'August']:
    print('The season is Summer')
else:
    print('That is not a valid month')

# 3: fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ').lower()
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)

# ---------------- Level 3 ----------------
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

# 1: middle skill
if 'skills' in person:
    skills = person['skills']
    print(skills[len(skills) // 2])      # Node

# 2: does the person have 'Python'?
if 'skills' in person:
    print('Python' in person['skills'])  # True

# 3: job title from skills
skills = person['skills']
if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')

# 4: married and lives in Finland
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")