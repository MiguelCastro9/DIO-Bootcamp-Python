# iterators and generators in python

# if the code is something simpler we use the generator, and if it is more complex code we use the iterator.

# ITERATORS
# an iterator is an object that contains a countable number of values ​​that can be iterated over, 
# which means you can loop through all the values. 
# the iterator protocol is a way for python to iterate an object, 
# which consists of two special methods "__iter__()" and __next__()".

class MyIterator:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers
        self.counter = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            number = self. numbers[self.counter]
            self.counter += 1
            return number * 2
        except IndexError:
            raise StopIteration

for i in MyIterator(numbers=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]):
    print(i)


# GENERATORS
# are special types of iterators, unlike lists or other iterables, they do not store all their values ​​in memory.
# are defined using regular functions, but instead of returning values ​​using "return", they use "yield".

# - once a generated item is consumed, it is forgotten and cannot be accessed again.
# - the internal state of a generator is maintained between calls.
# - the execution of a generator is paused at the "yield" statement and resumed from there the next time it is called.

def my_gerator(numbers: list[int]):
    for number in numbers:
        yield number * 2

for i in my_gerator(numbers=[1, 2, 3]):
    print(i)