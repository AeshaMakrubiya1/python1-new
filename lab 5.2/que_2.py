'''
create tuple of 5 numbers.
- Access the third item in the tuple.
- Try to change the second value and observe the result.(explain mutability.)
'''

numbers = (10, 20, 30, 40, 50)

print("Third item:", numbers[2])

try:
    numbers[1] = 99
except TypeError:
    print("Error: Tuples are immutable (cannot change values).")