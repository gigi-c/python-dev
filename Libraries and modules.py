# LIBRARIES AND MODULES
import random  # import then follow by the name of the library
import math

print(random.random())
num_float = 23.66
print(math.ceil(num_float))  # round up
print(math.floor(num_float))  # round down

# python makes use of modules and bring it into your own programme
# import xxx from xxx
# connect to external sources (web data)

import requests

request_bbc = requests.get("http://www.bbc.co.ul/")
print(request_bbc.status_code)
print(request_bbc.content)
