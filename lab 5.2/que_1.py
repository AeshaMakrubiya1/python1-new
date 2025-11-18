'''
create a list of 5 fruits. print the second and last fruit.
- Access the third item in the tuple.
- sort the list alphabetically. Reversed it.
'''

fruits = ["Apple", "Banana", "Orange", "Grapes", "Kiwi"]

print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

fruits.append("Mango")

fruits.pop(0)

fruits.sort()

fruits.reverse()

print("Final list:", fruits)