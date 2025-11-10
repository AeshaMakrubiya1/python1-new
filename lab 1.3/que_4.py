# write a python program to:
# - Declare a variable of each datatype(ineger, float, string, boolean, list, tuple, dictionary).
# - Print the value, type(using type()), and memory address(using id()) of each variable.

a = 10
b = 5.5
c = "Hello"
d = True
e = [1, 2, 3]
f = [4, 5, 6]
g = {"name": "Aesha"}

variables = [a, b, c, d, e, f, g]

for v in variables:
    print("Value:", v, "| Type:", type(v), "| Memory Address:", id(v))