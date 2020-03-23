# LAMBDA FUNCTION
# essentially anonymous function that can take multiple parameters but return only one expression

# normal way to declare a function:
def add(num1, num2):
    return num1 + num2
print(add(23, 45))

# lamda function:
addition = lambda num1, num2: num1 + num2
print(addition(23, 45))

savings = [234, 567, 674, 78]
bonus = list(map(lambda x: x * 1.1, savings)) # map picks up the value x and multiply to 1.1 and
                                              # replace the orginal savings then return the value
print(bonus)

