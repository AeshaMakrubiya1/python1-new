'''
Implement a program where a UDF accepts a list of integers and returns the square of each integer in a new list using a list comprehension.
'''
def square_list(numbers):
    """Return a new list containing the square of each integer."""
    return [num ** 2 for num in numbers]

# Example usage:
nums = [2, 4, 6, 8]
squared = square_list(nums)

print("Original list:", nums)
print("Squared list:", squared)
