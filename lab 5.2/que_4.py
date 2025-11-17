'''
create a list of square of numbers from 1 to 10 using list comprehension.
-create a new list that only contains even numbers from a given list 91,2,3,.....,20
- convert all strings in a list ["hello", "WORLD", "PyThOn"] to lowercase using list comprehension.
'''

squares = [x*x for x in range(1, 11)]
print(squares)

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

words = ["hello", "WORLD", "PyThOn"]
lowercase = [w.lower() for w in words]
print(lowercase)