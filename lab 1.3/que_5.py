# Create a program that:
# - Declares two variables with the same value.
# - Prints their memory addresses using id() and checks if they are the same.
# - Modifies one of the variables and checks the memory addresses again.

a = 10
b = 10

print("Before modification:")
print("a =", a, "|id(x):", id(a))
print("b =", b, "|id(b):", id(b))
print("Are both same?", id(a) == id(b))

a = 20

print("\nAfter modification:")
print("a =", a, "| id(a):", id(a))
print("b =", b, "| id(b):", id(b))
print("Are both same now ?", id(a) == id(b))