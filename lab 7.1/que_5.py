'''
create a program that takes a user-defined function as an argument to calculate the cube of a list of numbers 
'''

def cube(n):
    return n ** 3

def apply_function(num_list, func):
    result = []
    for n in num_list:
        result.append(func(n))
    return result

numbers = [1, 2, 3, 4, 5]

output = apply_function(numbers, cube)

print("Original list:", numbers)
print("Cubes:", output)
