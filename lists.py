# lists em python

fruits = ['grape', 'apple', 'pear']
print(fruits)

separate_letters = list('python')
print(separate_letters)

car = ['BMW', 2024, 80000, '320I', True]
print(car)

matrix = [
    [1, 'A', 2],
    ['B', 3, 4],
    ['C', 5, 6]
]
print(matrix[0][0])
print(matrix[2][2])


# methods of list

numbers = list(range(10))
pairs = []
for n in numbers:
    if n % 2 == 0:
        pairs.append(n)
print(pairs)

products = ['keyboard', 'mouse', 'monitor']
products.clear()
print(products)

group = [1, 'QA', ['fulano', 'ciclano', 'beutrano']]
time = group.copy()
print(time)

languages = ['java', 'python', 'c#', 'java', 'java']
print(languages.count('java'))

courses = ['inglês', 'mathematics', 'biology']
courses.extend(['programation'])
print(courses)

print(courses.index('biology'))

courses.pop(3)
print(courses)

courses.remove('mathematics')
print(courses)

languages.reverse()
print(languages)

letters = ['C', 'B', 'A']
letters.sort()
print(letters)