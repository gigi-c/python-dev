# 16 March 2020
# Exercise 1: user input detail
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
address = input("What is the first line of your address? ")
postcode = input("What is your post code? ")
birthday = input("When is your birthday? ")
age = input("How old are you? ")

print("Hello", first_name, last_name, ", you are living at", address, postcode,
      ". Your birthday is on", birthday, "and your are now", age, "years old.")

# Exercise 2: palindrome
text = input("Enter a word: ")
reverse_text = text [: : -1]
print(reverse_text)
print(text.lower() == reverse_text.lower())

# Exercise 3: number odd or even
a = int(input("Enter a number: "))
if(a%2 == 0):
    print("{} is an even number".format(a))
else:
    print("{} is an odd number".format(a))

# Exercise 4: biggest of 3 numbers
a = input("Please enter the first number: ")
b = input("Please enter the second number: ")
c = input("Please enter the third number: ")
if (a > b and a > c):
    print("{} is the biggest amongst {}, {} and {}".format(a, a, b, c))
elif (b > a and b > c):
    print("{} is the biggest amongst {}, {} and {}".format(b, a, b, c))
elif (c > a and c > b):
    print("{} is the biggest amongst {}, {} and {}".format(c, a, b, c))
else:
    print("one or more values are equal")

# 17 March 2020
# Exercise 1: sorting into odd / even lists
num_list = [10, 111, 24, 56, 78, 75, 65, 80]
odd_list = []
even_list = []
for num in num_list:
    if num%2 == 1:
        odd_list.append(num)
    else:
        even_list.append(num)
print(odd_list)
print(even_list)

# Exercise 2: Fizzbuz
number = int(input("Please enter a number: "))
if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
elif number%3 == 0:
    print("Fizz")
elif number%5 == 0:
    print("Buzz")
else:
    print("{} is not divisible by both 3 and 5".format(number))

# or range of numbers
number = int(input("Please enter a number: "))
for num in range (1,number + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("{} is not divisible by both 3 and 5".format(num))
