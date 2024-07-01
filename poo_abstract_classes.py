# POO - abstract classes in python

# by default, Python does not provide abstract classes. 
# python comes with a module that provides the basis for defining abstract classes, and the name of the module is ABC. 
# ABC works by decorating base class methods as abstract and then 
# registering concrete classes as implementations of the abstract base. 
# a method becomes abstract when decorated with @abstractmethod.

# this way we have more security when using polymorphism.

from abc import ABC, abstractmethod

class RemoteControl(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class ControlTV(RemoteControl):

    def turn_on(self):
        print("turning on TV...")
        print( "TV on!")

    def turn_off(self):
        print("turning off TV...")
        print("TV off!")

controle = ControlTV()
controle.turn_on()