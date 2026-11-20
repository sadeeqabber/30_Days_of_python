# Day 1: 30 Days of python programming

# ---------------- Level 1 / Level 2 ----------------

# Python version (also try "python --version" in the terminal)
import sys
print(sys.version)

# Operations with the operands 3 and 4
print('Addition:', 3 + 4)
print('Subtraction:', 3 - 4)
print('Multiplication:', 3 * 4)
print('Modulus:', 3 % 4)
print('Division:', 3 / 4)
print('Exponential:', 3 ** 4)
print('Floor division:', 3 // 4)

# Strings
print('Muhammad')
print('Abubakar')
print('Nigeria')
print('I am enjoying 30 days of python')

# Data types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Amina'))
print(type('Bello'))
print(type('Nigeria'))

# ---------------- Level 3 ----------------

# One example of each data type
integer = 25
decimal = 1.75
complex_number = 2 + 3j
text = 'Python'
is_learning = True
skills = ['Python', 'Excel', 'SQL']
coordinates = (2, 3)
unique_numbers = {1, 2, 3}
person = {'name': 'Amina', 'country': 'Nigeria'}

for value in [integer, decimal, complex_number, text, is_learning,
              skills, coordinates, unique_numbers, person]:
    print(value, '->', type(value))

# Euclidean distance between (2, 3) and (10, 8)
# distance = square root of ((x2 - x1)^2 + (y2 - y1)^2)
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('Euclidean distance:', distance)