# write a python program to demonstrate the use of the type casting constructors(int(), float(), str(), and bool()):
# - Take input from the user as a string.
# - Convert the string into an integer, a float, and a boolean.
# - Print the converted values along with their types.

user_input = input("Enter a number : ")

int_value = int(user_input)
float_value = float(user_input)
bool_value = bool(user_input)

print("Integer:", int_value, type(int_value))
print("Float:", float_value, type(float_value))
print("Boolean:", bool_value,type(bool_value))