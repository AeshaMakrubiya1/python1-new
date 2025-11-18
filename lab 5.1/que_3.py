'''implement a program to:
- take a string as input.
- print the string reserved, and also priont wheather it is a palindrome.
'''

s = input("Enter a string: ")
rev = s[::-1] 
print("reversed:", rev)

if s == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")