def biggest_number(a, b, c):
    if a > b and a > c:
        print("{} is the biggest.".format(a))
    elif b > a and b > c:
        print("{} is the biggest.".format(b))
    elif c > a and c > b:
        print("{} is the biggest.".format(c))
    else:
        print("one or more number is equal")

biggest_number(12, 3, 40)
