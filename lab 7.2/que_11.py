'''
Implement a program to modify a global variable that stores a username.
-use a function to update the name based on user input.
'''

username = "Guest"   # Global variable

def update_username():
    global username   # Allow modification of global variable
    new_name = input("Enter new username: ")
    username = new_name   # Update the global variable


# Before update
print("Current username:", username)

# Update username
update_username()

# After update
print("Updated username:", username)
