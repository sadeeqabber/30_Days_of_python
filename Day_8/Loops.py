# Day 8: 30 Days of python programming
# Level 3 needs countries.py and countries_data.py in the same folder as this file.
# (countries_data.py is the course data file with the line "countries_data = " added at the top.)
from countries_data import countries_data

# Use the country names already available in countries_data instead of requiring
# a separate countries.py module.
countries = [country['name'] for country in countries_data]

# ---------------- Level 1 ----------------

# 1: 0 to 10 with for, then with while
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# 2: 10 to 0
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

# 3: triangle with seven calls to print()
for i in range(1, 8):
    print('#' * i)

# 4: 8 x 8 grid with nested loops
for row in range(8):
    line = ''
    for column in range(8):
        line += '# '
    print(line.strip())

# 5: squares pattern
for i in range(11):
    print(f'{i} x {i} = {i * i}')

# 6: loop through a list
for item in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(item)

# 7: even numbers 0 to 100
for i in range(101):
    if i % 2 == 0:
        print(i)

# 8: odd numbers 0 to 100
for i in range(101):
    if i % 2 != 0:
        print(i)

# ---------------- Level 2 ----------------

# 1: sum of 0 to 100
total = 0
for i in range(101):
    total += i
print(f'The sum of all numbers is {total}.')

# 2: sum of evens and sum of odds
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f'The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.')

# ---------------- Level 3 ----------------

# 1: countries containing 'land'
for country in countries:
    if 'land' in country.lower():
        print(country)

# 2: reverse a list using a loop (build a new list, adding each item at the front)
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)

# 3.1: total number of distinct languages in the data

all_languages = set()
for country in countries_data:
    for language in country['languages']:
        all_languages.add(language)
print('Total number of languages:', len(all_languages))

# 3.2: ten most spoken languages
language_count = {}
for country in countries_data:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

# sorted() on (count, language) pairs, biggest first
pairs = []
for language, count in language_count.items():
    pairs.append((count, language))
pairs.sort(reverse=True)
print('Ten most spoken languages:')
for count, language in pairs[:10]:
    print(f'{language}: {count} countries')

# 3.3: ten most populated countries
by_population = []
for country in countries_data:
    by_population.append((country['population'], country['name']))
by_population.sort(reverse=True)
print('Ten most populated countries:')
for population, name in by_population[:10]:
    print(f'{name}: {population}')