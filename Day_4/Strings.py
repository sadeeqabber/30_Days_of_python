# Day 4: 30 Days of python programming

# 1: join four words with + (the ' ' adds the spaces)
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# 2
print('Coding' + ' ' + 'For' + ' ' + 'All')

# 3-5: company variable, print it, print its length
company = 'Coding For All'
print(company)
print(len(company))

# 6-7: upper and lower case
print(company.upper())
print(company.lower())

# 8: capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9: slice out the first word (index 0 up to, but not including, 6)
print(company[0:6])

# 10: does it contain 'Coding'?
print(company.find('Coding'))
print(company.index('Coding'))
print('Coding' in company)

# 11: replace Coding with Python
print(company.replace('Coding', 'Python'))

# 12: Python for Everyone -> Python for All
print('Python for Everyone'.replace('Everyone', 'All'))

# 13: split on spaces
print(company.split())

# 14: split at the comma (the separator is a comma AND a space)
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

# 15-17: indexes
print(company[0])
print(len(company) - 1)
print(company[10])

# 18-19: acronyms (first letter of each word)
words = 'Python For Everyone'.split()
print(words[0][0] + words[1][0] + words[2][0])
words = company.split()
print(words[0][0] + words[1][0] + words[2][0])

# 20-21: index of first C and first F
print(company.index('C'))
print(company.index('F'))

# 22: last l in 'Coding For All People'
print('Coding For All People'.rfind('l'))

# 23-27: the 'because' sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))
start = sentence.index('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

# 28: starts with Coding?
print(company.startswith('Coding'))
print("'Coding For All".startswith('Coding'))

# 29: ends with 'coding'? (case matters)
print(company.endswith('coding'))

# 30: remove spaces from both ends (inside spaces stay)
spaced = '   Coding For All      '
print(spaced.strip())

# 31: which are valid variable names?
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32: join with '# '
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# 33: new line escape sequence
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34: tab escape sequence
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 35: string formatting (f-string)
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')

# 36: operations table (:.2f gives 2 digits after the decimal point)
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')