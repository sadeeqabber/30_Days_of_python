# Day 9: 30 Days of python programming - Functions (Levels 1-3)
# Level 3 needs countries_data.py in the same folder.
import keyword

from countries_data import countries_data

# ---------------- Level 1 ----------------

# 1
def add_two_numbers(a, b):
    return a + b

# 2
def area_of_circle(r):
    return 3.14 * r * r

# 3: *args collects any number of arguments into a tuple
def add_all_nums(*args):
    total = 0
    for item in args:
        # bool counts as int in Python, so exclude it explicitly
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            return f'Error: {item!r} is not a number'
        total += item
    return total

# 4
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# 5
def check_season(month):
    month = month.title()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    return 'Invalid month'

# 6: slope between two points
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return 'The slope is undefined (vertical line)'
    return (y2 - y1) / (x2 - x1)

# 7: ax^2 + bx + c = 0 using the quadratic formula
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return 'Not a quadratic equation (a cannot be 0)'
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return 'No real solutions'
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    return {root1, root2}            # a set, so a double root appears once

# 8
def print_list(lst):
    for item in lst:
        print(item)

# 9: reverse with a loop (insert each item at the front of a new list)
def reverse_list(lst):
    result = []
    for item in lst:
        result.insert(0, item)
    return result

# 10
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11: returns a NEW list, so the original is not changed
def add_item(lst, item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list

# 12
def remove_item(lst, item):
    new_list = lst.copy()
    if item in new_list:
        new_list.remove(item)
    return new_list

# 13: 1 + 2 + ... + n
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 14
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total

# 15
def sum_of_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

# ---------------- Level 2 ----------------

# 1: counts evens and odds from 0 up to and including n
def evens_and_odds(n):
    odds = 0
    evens = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f'The number of odds are {odds}.\nThe number of evens are {evens}.'

# 2
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 3
def is_empty(value):
    if value is None:
        return True
    try:
        return len(value) == 0       # works for str, list, tuple, set, dict
    except TypeError:
        return False                 # numbers have no length, so they are not "empty"

# 4: statistics on a list of numbers
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    ordered = sorted(lst)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2

def calculate_mode(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    highest = max(counts.values())
    modes = [item for item in counts if counts[item] == highest]
    return modes[0] if len(modes) == 1 else modes   # a list if there is a tie

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):         # population variance (divide by n)
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):              # standard deviation = square root of variance
    return calculate_variance(lst) ** 0.5

# ---------------- Level 3 ----------------

# 1: prime = greater than 1 and divisible only by 1 and itself
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2: all unique? a set drops duplicates, so lengths differ if there are any
def all_unique(lst):
    return len(lst) == len(set(lst))

# 3: all the same data type?
def same_type(lst):
    for item in lst:
        if type(item) != type(lst[0]):
            return False
    return True

# 4: valid python variable name?
def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

# 5: most spoken languages and most populated countries
def most_spoken_languages(data, n=10):
    counts = {}
    for country in data:
        for language in country['languages']:
            counts[language] = counts.get(language, 0) + 1
    pairs = [(count, language) for language, count in counts.items()]
    pairs.sort(reverse=True)
    return [(language, count) for count, language in pairs[:n]]

def most_populated_countries(data, n=10):
    pairs = [(country['population'], country['name']) for country in data]
    pairs.sort(reverse=True)
    return [(name, population) for population, name in pairs[:n]]

# ---------------- Testing the functions ----------------
if __name__ == '__main__':
    print(add_two_numbers(2, 3))                              # 5
    print(area_of_circle(10))                                 # 314.0
    print(add_all_nums(1, 2, 3.5), add_all_nums(1, 'a'))      # 6.5 and an error message
    print(convert_celsius_to_fahrenheit(100))                 # 212.0
    print(check_season('june'))                               # Summer
    print(calculate_slope(2, 2, 6, 10))                       # 2.0
    print(solve_quadratic_eqn(1, 6, 9), solve_quadratic_eqn(1, -3, 2), solve_quadratic_eqn(1, 0, 1))
    print_list(['a', 'b'])
    print(reverse_list([1, 2, 3, 4, 5]), reverse_list(['A', 'B', 'C']))
    print(capitalize_list_items(['python', 'flask']))
    print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Meat'), add_item([2, 3, 7, 9], 5))
    print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'), remove_item([2, 3, 7, 9], 3))
    print(sum_of_numbers(5), sum_of_numbers(10), sum_of_numbers(100))   # 15 55 5050
    print(sum_of_odds(10), sum_of_even(10))                   # 25 30
    print(evens_and_odds(100))
    print(factorial(5))                                       # 120
    print(is_empty([]), is_empty('hi'), is_empty(None), is_empty(0))
    data = [2, 4, 4, 5, 7, 9]
    print(calculate_mean(data), calculate_median(data), calculate_mode(data),
          calculate_range(data), calculate_variance(data), calculate_std(data))
    print(is_prime(7), is_prime(10), is_prime(1))
    print(all_unique([1, 2, 3]), all_unique([1, 2, 2]))
    print(same_type([1, 2, 3]), same_type([1, 'a']))
    print(is_valid_variable('first_name'), is_valid_variable('1name'), is_valid_variable('for'))
    print(most_spoken_languages(countries_data))
    print(most_populated_countries(countries_data))