# Day 3: 30 Days of python programming

# 1-3: age (int), height (float), complex number
age = 30
height = 1.75
complex_number = 2 + 3j
print('Age:', age, type(age))
print('Height:', height, type(height))
print('Complex number:', complex_number, type(complex_number))

# 4: area of a triangle
base = float(input('Enter base: '))
tri_height = float(input('Enter height: '))
area_of_triangle = 0.5 * base * tri_height
print('The area of the triangle is', area_of_triangle)

# 5: perimeter of a triangle
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
perimeter_of_triangle = side_a + side_b + side_c
print('The perimeter of the triangle is', perimeter_of_triangle)

# 6: rectangle area and perimeter
length = float(input('Enter length: '))
width = float(input('Enter width: '))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print('Area of rectangle:', area_of_rectangle)
print('Perimeter of rectangle:', perimeter_of_rectangle)

# 7: circle area and circumference (pi = 3.14)
pi = 3.14
radius = float(input('Enter radius: '))
area_of_circle = pi * radius * radius
circum_of_circle = 2 * pi * radius
print('Area of circle:', area_of_circle)
print('Circumference of circle:', circum_of_circle)

# 8: y = 2x - 2  (compare with y = mx + c)
slope = 2
y_intercept = -2
x_intercept = 2 / 2
print('Slope:', slope)
print('x-intercept:', x_intercept)
print('y-intercept:', y_intercept)

# 9: slope and Euclidean distance between (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('Slope between the points:', slope_2)
print('Euclidean distance:', distance)

# 10: compare the slopes from tasks 8 and 9
print('Slope 8 > slope 9:', slope > slope_2)
print('Slope 8 == slope 9:', slope == slope_2)

# 11: y = x^2 + 6x + 9, try different x values
x = -5
print('x =', x, ' y =', x ** 2 + 6 * x + 9)
x = -4
print('x =', x, ' y =', x ** 2 + 6 * x + 9)
x = -3
print('x =', x, ' y =', x ** 2 + 6 * x + 9)
x = 0
print('x =', x, ' y =', x ** 2 + 6 * x + 9)


# 12: lengths of 'python' and 'dragon', and a falsy (False) comparison
print(len('python'), len('dragon'))
print(len('python') != len('dragon'))

# 13: is 'on' found in both words?
print('on' in 'python' and 'on' in 'dragon')

# 14: is 'jargon' in the sentence?
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)

# 15: there is no 'on' in both dragon and python
print(not ('on' in 'dragon' and 'on' in 'python'))

# 16: length of 'python', then float, then string
length_of_python = len('python')
print(length_of_python)
print(float(length_of_python))
print(str(float(length_of_python)))

# 17: check if a number is even (divisible by 2, remainder 0)
number = 8
print(number, 'is even:', number % 2 == 0)
number = 7
print(number, 'is even:', number % 2 == 0)

# 18: floor division of 7 by 3 equals int(2.7)?
print(7 // 3 == int(2.7))

# 19: type of '10' equal to type of 10?
print(type('10') == type(10))

# 20: int('9.8') == 10 ?
print(int(float('9.8')) == 10)

# 21: weekly earning
hours = float(input('Enter hours: '))
rate_per_hour = float(input('Enter rate per hour: '))
weekly_earning = hours * rate_per_hour
print('Your weekly earning is', weekly_earning)

# 22: seconds lived
years = float(input('Enter number of years you have lived: '))
seconds = years * 365 * 24 * 60 * 60   # days, hours, minutes, seconds
print('You have lived for', int(seconds), 'seconds.')

# 23: the table
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)