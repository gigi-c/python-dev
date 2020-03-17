# Exercise
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