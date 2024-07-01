# set in python

# 'set' is a collection that does not store repeated values.
numbers = set([1, 2, 3, 4, 5, 5, 6, 6])
print(numbers)

word = set('abacaxi')
print(word)

set_a = {1, 2, 3}
set_b = {4, 5, 6}
print(set_a.union(set_b))

set_c = {1, 2, 3}
set_d = {4, 2, 5}
print(set_c.intersection(set_d))

set_e = {1, 2, 3}
set_f = {1, 2, 4}
print(set_e.difference(set_f))

set_g = {1, 2, 3}
set_h = {1, 2, 4}
print(set_g.symmetric_difference(set_h))

sortition = {1, 23}
sortition.add(34)
sortition.add(59)
sortition.add(23)
print(sortition)