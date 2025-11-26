'''
Implement a recursion function to calculate the nth fibonacci number.
-Test the function with various inputs.
'''

def fibonacci(n):
    # Handle negative inputs
    if n < 0:
        return "Fibonacci is not defined for negative numbers."

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


# Testing the function
print("fibonacci(0):", fibonacci(0))
print("fibonacci(1):", fibonacci(1))
print("fibonacci(5):", fibonacci(5))
print("fibonacci(10):", fibonacci(10))
print("fibonacci(-3):", fibonacci(-3))
