# Three Types of Control Flow
# 1. If statements
# 2. For statements
# 3. While loop

# IF STATEMENTS
'''
age = 25
if age < 19:
    print("You are note eligible to watch this film.") #indentation is very important
else:
    print("You are good to go.")
'''
film_rating = input("What is the film rating? ")
if film_rating.lower() == "universal":
    print("All age groups can watch this film.")
elif film_rating.lower() == "pg":
    print("General viewing, but some scenes mau be unsutable for young children.")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contained material that is not generally suitable for "
          "children aged under 12. No one younger than 12 may see a 12A"
          " film in a cinema unless accompanied by an adult.")
elif film_rating.lower() == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
elif film_rating.lower() == "18":
    print("No one younger than 18 may see an 18 film in a cinema")
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")

# if number is divisible by 3 or 5
number = int(input("Please enter a number: "))
if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
elif number%3 == 0:
    print("Fizz")
elif number%5 == 0:
    print("Buzz")
else:
    print("{} is not divisible by both 3 and 5".format(number))

#or range of numbers
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

# FOR LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
for x in "banana": #checking character by character
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break #adding a break so it is not printing

for x in range(6): #from 0 up to the number you enter
    print(x)
else: #else can be used with for loop
    print("Finally finished!")

#using 2 for loops to print both list
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj: #taken the first value move on to next inner loop and print all the values in the inner loop
    for y in fruits:
        print(x, y)

list_data = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3,66"},
             3: {"name": "Roscoe", "money": "$1,14"}}

for num in list_data:
    print(num*2)

for data in embedded_list:
    print(data)
    for num in (data):
        print(num)

# Nested loop
for value in dict_data: #first for loop will be fetching the key from the outer dictionary
    print(value)
for item in dict_data.values(): #get value for the outer key (i.e all the inner dictionaries)
     print(item)
for item in dict_data.values():
    for embed_value in item.values(): #give the values of the inner dictionaries without the keys
        print(embed_value)

# WHILE LOOP
x = 0 #initialisng the variable
while x < 10: #condition
    print("its working --> {}".format(x))
    x = x + 1

while x < 10:
    print("its working --> {}".format(x))
    if x == 4:
        break
    x = x + 1