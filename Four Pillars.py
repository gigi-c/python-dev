# Four pillars of Object oriented programming
# Abstraction : displaying only essential information to the user and hiding the details from the user

from animal import Animal # can use * as well which means fetch everything from animal.py
                          # this step hide all the class code from the users
Dog1 = Animal("Nyme", 10)
Dog2 = Animal("Mone", 5)
print(Dog1.name)

# Inheritance: a mechanism in which one class acquires the property of another class
from animal import *
class Reptile(Animal): #the reptile class (child) inheriting from the animal class (parent)
    def __init__(self, name, age):
        super().__init__(name, age) # this super command is a must for inheritance such that everything from the
                                    # parent (animal) is brought to the child (reptile)

    def sleep(self):
        return ("zzzz I am sleeping")
    def running(self, speed):
        return ("I am running in {} speed", speed)

Rept1 = Reptile("Lizzard", 5)
Rept2 = Reptile("Mosy", 8)
print(Rept1.eat())
# Encapsulation
# Polymerisation
