'''
split "apple,banana,grapes" into a list.
- join the list ["python", "is", "awesome"] into a sentence using spaces.
- split a multiline string into separate lines and print them one by one.
'''

fruits = "apple,banana,grapes".split(",")
print(fruits)

words = ["Python", "is", "awesome"]
print(" ".join(words))

multi = "Hello\nWorld\nPython"
for line in multi.split("\n"):
    print(line)