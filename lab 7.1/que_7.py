'''
Implement a function that takes a list of student names using *args and prints each name on a new line.
- Add functionally to check if the list is empty and display a suitable message.
'''

def print_students(*names):
    if len(names) == 0:
        print("No student names were provided.")
    else:
        print("Student Names:")
        for name in names:
            print(name)

# Example usage
print_students("Aesha", "darshan", "mansi")

print()  # blank line

print_students()  # calling with no names
