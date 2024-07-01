# POO - herance in python

class Vehicle:
    def __init__(self, name, brand, color, plate):
        self.name = name
        self.brand = brand
        self.color = color
        self.plate = plate

    def turn_on_engine(self):
        print("engine on!")

    def __str__(self):
        return f"Vehicle: name={self.name} brand={self.brand} color={self.color} plate={self.plate}"

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

car = Car("320i", "BMW", "preta", "abc-123")
motorcycle = Motorcycle("xj6", "honda", "preta", "123-abc")

print(car)
print(motorcycle)
car.turn_on_engine()
motorcycle.turn_on_engine()
