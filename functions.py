# functions in python

def message():
    print('hello world!')
message()

def sum_numbers(n1, n2):
    print('the sum is: ', n1 + n2)
sum_numbers(n1=5, n2=5)

def multiplication(n1, n2):
    return n1 * n2

def show_result(n1, n2, function):
    result = function(n1, n2)
    print('the multiplication is: ', result)

show_result(5, 5, multiplication)

# *Args e **Kwargs
# *Args it will treat as a tuple
# **Kwargs it will treat as a dictionary

# *Args
def sum_all(*args):
    return sum(args)
# calling the function with different number of arguments
print(sum_all(1, 2, 3)) 
print(sum_all(4, 5, 6, 7, 8))

# **Kwargs
def show_information(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

# calling the function with different named arguments
show_information(name='Miguel Castro', age=24, city='Malta - Sliema')

# *Args e **Kwargs
def function_complete(*args, **kwargs):
    print('arguments positional:', args)
    print('arguments nominated:', kwargs)

# calling the function with positional and named arguments
function_complete(1, 2, 3, name='Maria', age=25)