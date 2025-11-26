'''
create a program that uses a global variable to count the number of times a spesific function is called.
'''

largest = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

# Testing the function
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest number:", largest(x, y, z))
