# Create a program that:
#  - Takes a boolean value(True or False)as input.
#  - Convers the boolean to an integer and a string, and prints all three values.

bool_value= input("Enter True or False: ")
bool_value= bool_value == "True"

int_value = int(bool_value)
str_value = str(bool_value)

print("Boolean:", bool_value)
print("As Integer:", int_value)
print("As String:", str_value)