# Set is a collection that is unordered and unindexed
# Sets are written with {curly brackets}

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

car_parts.add("windows")
print(car_parts)

car_parts.discard("doors")
print(car_parts)

#Frozen sets: immutable versions of the set similar to tuple
x = frozenset([1, 2, 3, 5])
print(type(x))