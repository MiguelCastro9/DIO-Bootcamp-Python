# POO - polymorphism in python

class Bird:
    def fly(self): pass

class Sparrow(Bird):
    def fly(self):
        print ("Sparrow fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich dont fly")

def plan_of_flight(bird):
    bird.fly()


b1 = plan_of_flight(Sparrow())
b2 = plan_of_flight(Ostrich())