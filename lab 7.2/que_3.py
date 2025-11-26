'''
develop a program using recursion to reverse a string.
'''

def reverse_string(s):
    # Base case: if string is empty or has 1 character
    if len(s) <= 1:
        return s

    # Recursive case: last character + reverse of the remaining string
    return s[-1] + reverse_string(s[:-1])


# Testing the function
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
