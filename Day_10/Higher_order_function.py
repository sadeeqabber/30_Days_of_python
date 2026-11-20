# Day 10: 30 Days of python programming - Higher order functions

from functools import reduce

from countries_data import countries_data

all_countries = [country['name'] for country in countries_data]

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ---------------- Level 1 ----------------

# 1: map, filter and reduce
# map(f, items)    -> applies f to EVERY item and gives back the same number of items
# filter(f, items) -> keeps only the items for which f returns True (fewer or equal items)
# reduce(f, items) -> combines all items into ONE single value (needs: from functools import reduce)

# 2: higher order function, closure, decorator
# higher order function: a function that takes a function as a parameter and/or returns one
# closure: an inner function that remembers variables of the outer function that made it
# decorator: a higher order function that wraps another function to add behaviour,
#            written with @name above the function

# 3: named ("call") functions defined before using map, filter and reduce
def square(x):
    return x ** 2

def is_even(x):
    return x % 2 == 0

def add_two_nums(x, y):
    return x + y

print(list(map(square, numbers)))
print(list(filter(is_even, numbers)))
print(reduce(add_two_nums, numbers))

# 4-6: for loops
for country in countries:
    print(country)
for name in names:
    print(name)
for number in numbers:
    print(number)

# ---------------- Level 2 ----------------


# 1-3: map
print(list(map(lambda c: c.upper(), countries)))
print(list(map(lambda n: n ** 2, numbers)))
print(list(map(lambda n: n.upper(), names)))

# 4-7: filter
print(list(filter(lambda c: 'land' in c, countries)))
print(list(filter(lambda c: len(c) == 6, countries)))
print(list(filter(lambda c: len(c) >= 6, countries)))
print(list(filter(lambda c: c.startswith('E'), countries)))

# 8: chain map -> filter -> reduce (square, keep even squares, add them up)
squares = map(lambda n: n ** 2, numbers)
even_squares = filter(lambda n: n % 2 == 0, squares)
print(reduce(lambda a, b: a + b, even_squares))

# 9: only the strings from a list
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))
print(get_string_lists([1, 'a', 2.5, 'Python', True, ['x']]))

# 10: reduce to sum the numbers
print(reduce(lambda a, b: a + b, numbers))

# 11: reduce to build the sentence
text = reduce(lambda a, b: a + ', ' + b, countries[:-1])
print(text + ', and ' + countries[-1] + ' are north European countries')

# 12: countries with a common pattern ('land', 'ia', 'island', 'stan')
def categorize_countries(pattern):
    return list(filter(lambda c: pattern in c.lower(), all_countries))
print(categorize_countries('land'))
print(categorize_countries('stan'))
print(len(categorize_countries('ia')))

# 13: dictionary of starting letter -> number of countries
def count_by_first_letter(lst):
    result = {}
    for country in lst:
        letter = country[0]
        result[letter] = result.get(letter, 0) + 1
    return result
print(count_by_first_letter(all_countries))

# 14-15: first ten and last ten countries
def get_first_ten_countries():
    return all_countries[:10]

def get_last_ten_countries():
    return all_countries[-10:]

print(get_first_ten_countries())
print(get_last_ten_countries())

# ---------------- Level 3 ----------------
# sorted(items, key=function): s

by_name = sorted(countries_data, key=lambda c: c['name'])
by_capital = sorted(countries_data, key=lambda c: c.get('capital', ''))
by_population = sorted(countries_data, key=lambda c: c['population'])

print([c['name'] for c in by_name[:5]])

print([c['capital'] for c in by_capital if c['capital']][:5])
print([(c['name'], c['population']) for c in by_population[:5]])

# ten most spoken languages
language_count = {}
for country in countries_data:
    for language in country['languages']:
        language_count[language] = language_count.get(language, 0) + 1
top_languages = sorted(language_count.items(), key=lambda pair: pair[1], reverse=True)[:10]
print(top_languages)

# ten most populated countries
top_populated = sorted(countries_data, key=lambda c: c['population'], reverse=True)[:10]
print([(c['name'], c['population']) for c in top_populated])