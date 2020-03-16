a = 24
b = 16
# print(a + b)
# print(a - b)
# print(4 * "me")
# print(8%3)

# floatnum = 1.356
# intnum = 4
# name = "xyz"
# print(floatnum + intnum)
# print(str(intnum) + name)

#creating strings
# single_quotes = 'Look! single quotes'
# double_quotes = "Look! double quotes"
# print(single_quotes)
# print(double_quotes)

# escape_example_1 = 'I said \'Wow!\''
# quote_in_quote = 'I said "Wow!"'
# reverse_quote_in_quote = "I said 'Wow!'"
# print(escape_example_1)
# print(quote_in_quote)
# print(reverse_quote_in_quote)

#count a substring within a string
#example_text = "Here's some text with lot's of text"
#print(example_text.count("text"))

#bring everthing to lowercase or uppercase or capitalise
# print(example_text.lower())
# print(example_text.upper())
# print(example_text.capitalize())

#replacing text
#print(example_text.replace("with", ","))

#Concatenation
# a = "here "
# b = "more "
# c = "much more"
# d = 10
# print(a + b + c, d)

#Concatenation & casting
# x = 2
# # # y = 5.4
# # # z = " there's now a number 25.4 unless we put a space in!"
# # # print(str(x) + str(y) + z)
# # # print(str(x) + " " + str(y) + z)

#string to numeric casting
# int_string = "6"
# print(int(int_string))
# print(type(int(int_string)))
#
# print(float(int_string))
# print(type(float(int_string)))

#Boolean & none
# a = True
# b = False
#
# print(a == b)
# print(a != b)
# print(a >= b)
# print(b <= a)

#Boolean methods within strings
# hi = "Hello World!"
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith("!"))
# print(hi.startswith("H"))

#Boolean value and numbers
# print true if there is a value, but false if there is no value
# x = -1
# y = 2
# print(bool(x))
# print(bool(y))
# print(bool(None))

#Reverser a string and whether it is palindrome
text = input("Enter a word: ")
reverse_text = text [: : -1]
print(reverse_text)
print(text.lower() == reverse_text.lower())