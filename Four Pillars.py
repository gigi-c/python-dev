# Four pillars of Object oriented programming
# Abstraction : displaying only essential information to the user and hiding the details from the user

from animal import Animal # can use * as well which means fetch everything from animal.py
                          # this step hide all the class code from the users
Dog1 = Animal("Nyme", 10)
Dog2 = Animal("Mone", 5)
# print(Dog1.name)

# Inheritance: a mechanism in which one class acquires the property of another class
# it allows you to call methods of the superclass in your subclass
# primary use case of this is to extend the functionality of the inherited method
from animal import *
class Reptile(Animal): #the reptile class (child) inheriting from the animal class (parent)
    def __init__(self, name, age):
        super().__init__(name, age) # this super command is a must for inheritance such that everything from the
                                    # parent (animal) is brought to the child (reptile)
                                    # let animal class to handle the arguments

    def sleep(self):
        return ("zzzz I am sleeping")
    def running(self, speed):
        return ("I am running in {} km/h".format(speed))

Rept1 = Reptile("Lizzard", 5)
Rept2 = Reptile("Mosy", 8)
print(Rept1.eat())
print(Rept1.running(10))
print(Rept2.sleep())

# Exercise
# class Teacher:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def talk(self, number):
#         return ("There are {} students in my class.".format(number))
#
# Teacher1 = Teacher("John", "Smith")
# Teacher2 = Teacher("Jane", "Leung")
# print(Teacher1.talk(17))
#
# class Student(Teacher):
#     def __init__(self, first_name, last_name, prog_language):
#         super().__init__(first_name, last_name)
#         self.prog_language = prog_language
#
#     def enjoy(self):
#         return ("{} enjoys to learn {}".format(self.first_name, self.prog_language))
#
#     def chill(self, hobby):
#         return ("{} likes to {}".format(self.first_name, hobby))
#
# student1 = Student("Rachel", "Green", "Python")
# student2 = Student("Lily", "Collin", "Java")
# print(student1.talk(20))
# print(student1.enjoy())
# print(student2.chill("read"))

# Encapsulation: restrict access to methods and variables, this can prevent the data from being modified by accident

class Snake(Reptile):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age
    def seek_heat(self):
        return ("Let me see some sunshine")

Sidney = Snake("DOO", 2)
print(Sidney.seek_heat())
# i don't want user to access eat method so need to go to animal class
# and add two underscore to the eat method def __eat(self):
print(Sidney.eat())

# Polymorphism: define methods in the child class that have the same name as the methods in the parent class
#               In inheritance, the child class inherits the methods from the parent class possible to modify
#                a method in a child class that it has inherited from the parent class (Method overriding)

class Snake(Reptile):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age
    def seek_heat(self):
        return ("Let me see some sunshine")
    def sleep(self): # the same snake method is in reptile but here the sleep method is modified and change the contact
        return ("Please leave me to sleep peacefully")
Sidney = Snake("DOO", 2)
print(Sidney.sleep())
