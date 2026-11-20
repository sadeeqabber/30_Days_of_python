# Day 2: 30 Days of python programming

# ---------------- Level 1 ----------------

# 3-9: basic variables
first_name = 'Muhammad'
last_name = 'Sadiq'
full_name = first_name + ' ' + last_name
country = 'Nigeria'
city = 'Kano'
age = 32
year = 2026

# 10-12: boolean variables
is_married = False
is_true = True
is_light_on = False

# 13: multiple variables in one line
name, home_country, home_city = 'Muhammad', 'Nigeria', 'Kano'

# ---------------- Level 2 ----------------

# 1: check the data type of every variable
print('--- Data types ---')
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2: length of first name
print('--- Lengths ---')
print('Length of first name:', len(first_name))

# 3: compare the length of first name and last name
print('Length of last name:', len(last_name))
print('First name longer than last name?', len(first_name) > len(last_name))
print('Same length?', len(first_name) == len(last_name))

# 4-11: arithmetic
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print('--- Arithmetic ---')
print('total:', total)
print('diff:', diff)
print('product:', product)
print('division:', division)
print('remainder:', remainder)
print('exp:', exp)
print('floor_division:', floor_division)

# 12: circle with radius 30 metres
pi = 3.14
radius = 30
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print('--- Circle ---')
print('Area of circle:', area_of_circle)
print('Circumference of circle:', circum_of_circle)

# 12.3: radius from user input

user_radius = float(input('Enter radius: '))
user_area = pi * user_radius ** 2
print('Area of circle with that radius:', user_area)

# 13: first name, last name, country and age
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Which country do you live in? ')
age = int(input('How old are you? '))
print(first_name, last_name, country, age)

# 14: reserved words (keywords) in Python
help('keywords')
