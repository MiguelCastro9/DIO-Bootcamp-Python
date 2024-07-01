# POO - classes in python

# defining class, attributes and methods
class Bicycle:
    # the __init__ is a special method that serves to reference a constructor within a class.
    def __init__(self, color, model, age, value):
        self.color = color
        self.model = model
        self.age = age
        self.value = value

    def honk(self):
        print("plim plim...")

    def stop(self):
        print("stoping the bicycle...")
        print("bicycle stop.")

    def run(self):
        print("vrummmm...")

    def __str__(self):
        return f"Bicycle: color={self.color} model={self.model} age={self.age} value={self.value}"


bicycle_01 = Bicycle("blue", "caloi", "2024", 2500)

bicycle_01.honk()
bicycle_01.stop()
bicycle_01.run()
print(bicycle_01)