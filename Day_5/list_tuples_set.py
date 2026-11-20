# Day 5: 30 Days of python programming
# Needs countries.py (from the course's data folder) in the same folder as this file.
from countries import countries

# LISTS - Level 1

# 1: empty list
empty_list = []

# 2: list with more than 5 items
numbers = [10, 20, 30, 40, 50, 60, 70]

# 3: length
print(len(numbers))

# 4: first, middle and last item
print(numbers[0])
print(numbers[len(numbers) // 2])
print(numbers[-1])

# 5: mixed data types: name, age, height, marital status, address
mixed_data_types = ['Amina', 30, 1.65, 'single', 'Kano, Nigeria']
print(mixed_data_types)

# 6-7: it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

# 8: number of companies
print(len(it_companies))

# 9: first, middle and last company
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# 10: modify one company, then print
it_companies[0] = 'Meta'
print(it_companies)

# 11: add a company at the end
it_companies.append('Tesla')

# 12: insert a company in the middle
it_companies.insert(len(it_companies) // 2, 'Netflix')
print(it_companies)

# 13: make one company uppercase
index = it_companies.index('Google')
it_companies[index] = it_companies[index].upper()
print(it_companies)

# 14: join with '#; '
print('#; '.join(it_companies))

# 15: does a company exist?
print('Apple' in it_companies)
print('Nokia' in it_companies)

# 16: sort (A to Z, changes the list itself)
it_companies.sort()
print(it_companies)

# 17: reverse (after sort(), this gives descending order)
it_companies.reverse()
print(it_companies)

# 18-19: first 3 and last 3
print(it_companies[:3])
print(it_companies[-3:])

# 20: middle company or companies
middle = len(it_companies) // 2
print(it_companies[middle])

# 21: remove the first
it_companies.pop(0)

# 22: remove the middle
it_companies.pop(len(it_companies) // 2)

# 23: remove the last
it_companies.pop()
print(it_companies)

# 24: remove all items
it_companies.clear()
print(it_companies)

# 25: destroy the list completely
del it_companies

# 26: join two lists with +
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27: copy the joined list and insert Python and SQL after Redux
full_stack = full_stack.copy()
position = full_stack.index('Redux') + 1
full_stack.insert(position, 'Python')
full_stack.insert(position + 1, 'SQL')
print(full_stack)


# LISTS - Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sort, min and max
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(ages, min_age, max_age)

# add the min and max again
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

# median
mid = len(ages) // 2
median = (ages[mid - 1] + ages[mid]) / 2
print('Median:', median)

# average and range
average = sum(ages) / len(ages)
age_range = max(ages) - min(ages)
print('Average:', average)
print('Range:', age_range)

# compare |min - average| and |max - average|
print(abs(min(ages) - average))
print(abs(max(ages) - average))

# middle country or countries
total_countries = len(countries)
if total_countries % 2 == 1:
    print(countries[total_countries // 2])
else:
    print(countries[total_countries // 2 - 1], countries[total_countries // 2])

# split countries into two lists
half = (total_countries + 1) // 2
first_half = countries[:half]
second_half = countries[half:]
print(len(first_half), len(second_half))

# unpack: first three countries, the rest are Scandinavian
nordic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = nordic
print(china, russia, usa)
print(scandic)


# TUPLES - Level 1


# 1: empty tuple
empty_tuple = ()

# 2-3: brothers and sisters (imaginary), joined with +
brothers = ('Musa', 'Ibrahim')
sisters = ('Aisha', 'Zainab')
siblings = brothers + sisters
print(siblings)

# 4: number of siblings
print(len(siblings))

# 5: tuples cannot change, so make a new tuple with the parents added
parents = ('Yusuf', 'Maryam')
family_members = siblings + parents
print(family_members)


# TUPLES - Level 2


# 1: unpack siblings and parents
*siblings, father, mother = family_members
print(siblings, father, mother)

# 2: join three tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
animal_products = ('milk', 'meat', 'butter', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products

# 3: change to a list
food_stuff_lt = list(food_stuff_tp)

# 4: middle item(s) - 13 items, so one middle item
mid = len(food_stuff_tp) // 2
print(food_stuff_tp[mid])

# 5: first three and last three
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# 6: delete the tuple
del food_stuff_tp

# 7: check items in a tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


# SETS

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Netflix', 'Tesla', 'Nvidia'])
it_companies.remove('Oracle')
print(it_companies)

# 5: remove vs discard
# remove() crashes with a KeyError if the item is not in the set.
# discard() does nothing if the item is not in the set.
it_companies.discard('Nokia')
# it_companies.remove('Nokia')

# Level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B) == B.union(A))
print(A.symmetric_difference(B))
del A
del B

# Level 3
age_set = set(age)
print(len(age), len(age_set))

# 2: string, list, tuple, set
# string : text, ordered, cannot change, has indexes   'abc'
# list   : ordered, CAN change, allows duplicates      [1, 2, 2]
# tuple  : ordered, cannot change, allows duplicates   (1, 2, 2)
# set    : unordered, no indexes, no duplicates        {1, 2}

# 3: unique words
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.replace('.', '').split()
print(len(words), len(set(words)))