'''
write a program to filter out odd numbers from a list using a lambda function and the filter() method.
'''

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() with lambda to keep only odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Odd numbers:", odd_numbers)
