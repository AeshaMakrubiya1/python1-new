# Write a python program to:
#  - Take a number as input from the user.
#  - Use an 'if-else' statement to check if the number is even or odd and print the result.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is odd")