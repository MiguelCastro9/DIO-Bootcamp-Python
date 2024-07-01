# POO - way to use static methods and methods in classes in python

class People:
    def __init__(self, name=None, age=None) :
        self.name = name
        self.age = age

    # I need access to the class context so I use a class method.
    @classmethod
    def create_from_birth_date(cls, age, month, day, name):
        age = 2024 - age
        return cls(name, age)
    
    # I don't need context, class or object instance so I use a static method.
    @staticmethod
    def is_bigger_age(age):
        return age >= 18
    
p = People.create_from_birth_date(1999, 7, 21, "Miguel Castro")

print(p.name, p.age)
print(People.is_bigger_age(18))
print(People.is_bigger_age(8))