'''
write a lambda function that accepts three numbers and returns the largest of the three.
'''

largest = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

# Testing the function
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest number:", largest(x, y, z))
