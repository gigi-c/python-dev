# a = 10
# b = 20
# if (a > b):
#     print("a is bigger")
# else:
#     print("b is bigger")

# a = input("Please enter the first number: ")
# b = input("Please enter the second number: ")
# if (a > b):
#     print("{} is bigger than {}".format(a,b))
# else:
#     print("{} is bigger than {}".format(b,a))

# a = input("Please enter the first number: ")
# b = input("Please enter the second number: ")
# c = input("Please enter the third number: ")
# if (a > b and a > c):
#     print("{} is the biggest amongst {}, {} and {}".format(a, a, b, c))
# elif (b > a and b > c):
#     print("{} is the biggest amongst {}, {} and {}".format(b, a, b, c))
# else:
#     print("{} is the biggest amongst {}, {} and {}".format(c, a, b, c))


a = int(input("Enter a number: "))
if(a%2 == 0):
    print("{} is an even number".format(a))
else:
    print("{} is an odd number".format(a))

