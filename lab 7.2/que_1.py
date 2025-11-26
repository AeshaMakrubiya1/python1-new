'''
write a recursive function to calculate the factorial of a given number.
- ensure the program handles edge cases(e.g., negative inputs).
'''
def factorial(n):
    # Handle negative numbers
    if n < 0:
        return "Factorial is not defined for negative numbers."

    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


# Example usage
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
