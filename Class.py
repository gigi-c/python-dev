# CLASSES
# A way of bringing both data and functionality together

# Define a class
# class Dog: # class name always has to start with CAPITAL
#     animal_kind = "canine" # class variable
#
#     # define a method (when a function is declared inside a class)
#     def bark(self): # self parameter is a reference to the current instance of the class, used to access variables that
#                     # belong to the class
#         return "woof"
# print(Dog.animal_kind)
# print(type(Dog))
# print(Dog.bark()) # error because no object, undefined self

# Exercise: Create a car class

# class Car:
#     model = "BMW"
#     def speed(self):
#         return "Good choice"
# print(Car.model)
# print(Car.speed(1))

# Exercise: Fizzbuzz
# class FizzBuzz:
#     def __init__(self, number):
#         self.number = number
#     def is_FizzBuzz(self):
#         if self.number % 3 == 0 and self.number % 5 == 0:
#             print("FizzBuzz")
#         elif self.number % 3 == 0:
#             print("Fizz")
#         elif self.number % 5 == 0:
#             print("Buzz")
#         else:
#             print(self.number)
#
# number_range = range(101)
# for n in number_range:
#     num1 = FizzBuzz(n)
#     num1.is_FizzBuzz()


# Creating object from class is instantiation
# only with the object you can run the method that declared inside the function

# class Dog:
#     animal_kind = "canine"
#
#     # whatever attribute you want the class to have will be given here
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # add two different methods for run amd jump
#     def run(self):
#         return ("{} can run.".format(self.name))
#     def jump(self):
#         return ("{} can jump.".format(self.name))
#     def bark(self):
#         return ("{} likes to woof.".format(self.name))
#
# # Create objects from the class
# x = Dog("Fido", 8) # whatever attribute the dog class has, x will inherit
# y = Dog("Dido", 3)
# print("THis is my dog", x.name + ".") # check if the value has been assigned
# print("It is", x.age, "years old.")
# print(x.run(), y.jump())
# print(x.bark(), y.bark())


# Creating a student class
class Student:
    student_type = "trainee"
    def __init__(self, name, course, week):
        self.name = name
        self.course = course
        self.week = week
    def enrol(self):
            return("{} attends the {} class".format(self.name, self.course))
    def trainer(self):
        if self.course == "Data 9":
            return("Isabella is the trainer for {}".format(self.course))
        elif self.course == "Engineer 52":
            return("Richard is the trainer for {}".format(self.course))
    def in_training(self):
        if self.week < 10:
            return("{} is on week {} of the training".format(self.name, self.week))
        elif self.week == 10:
            return("{} has finished the training".format(self.name))



a = Student("Gigi", "Data 9", 4)
b = Student("David", "Engineer 52", 10)
print(a.name, "and", b.name, "are", Student.student_type + "s.")
print(a.enrol())
print(a.trainer())
print(b.in_training())

