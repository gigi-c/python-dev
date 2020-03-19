# FUNCTIONS
# A special relationship where each input has single output
# Not exactly knowing what is inside the function like a black box

# Type 1 : without argument
# def hello(): # all function has to start with def, follow by the name of the function, () and end with :
#     print("Hello")
# hello()
#
# # Type 2: with arguments or parameters
# def func(a, b):
#     return a + b
# print("The sum is", func(10, 20))
# func(10,20) # show nothing because you the function itself does not contain a print statement so cannot call it
#
# # Type 3: with default arguments
# def func(a = 10, b = 30):
#     return a + b
# print("The sum is", func())
#
# # Type 4: with default and again passing the values
# def func(a = 10, b = 30):
#     return a + b
# print("The sum is", func(20, 40))

# Calculator operations
def add(a, b):
    return a + b
print(add(2, 6))

def multiplication(a, b):
    return a * b
print(multiplication(2, 6))

def subtraction(a, b):
    return a - b
print(subtraction(2, 6))

def division(a, b):
    return a/b
print(division(2, 6))