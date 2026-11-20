# Day 9: 30 Days of python programming - List comprehensions and lambda

# 1: keep only negative numbers and zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([n for n in numbers if n <= 0])

# 2: flatten a list of lists of lists
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([number for outer in list_of_lists for inner in outer for number in inner])

# 3: list of tuples (i, 1, i, i^2, i^3, i^4, i^5)
print([(i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)])

# 4: flatten, then build [COUNTRY, CODE, CITY] (code = first three letters)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[country.upper(), country[:3].upper(), city.upper()]
       for group in countries for country, city in group])

# 5: list of dictionaries
print([{'country': country.upper(), 'city': city.upper()}
       for group in countries for country, city in group])

# 6: concatenated names
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([first + ' ' + last for group in names for first, last in group])

# 7: lambda functions
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - m * x
print(slope(2, 2, 6, 10))
print(y_intercept(2, 2, 2))                     