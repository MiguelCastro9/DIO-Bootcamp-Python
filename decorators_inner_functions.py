# decorators - inner functions in python

# it is possible to define functions inside other functions, such functions are called internal functions.

def father():
    print("writing from the father() function")
    
    def son_1():
        print("writing the son_1() function")
    
    def son_2():
        print("writing the son_2() function")

    son_1()
    son_2()

father()