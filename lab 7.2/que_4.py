'''
write a recursive function to find sum of all digits of a given number until a single-digit number remains
'''

def sum_to_single_digit(n):
    # Convert negative number to positive
    n = abs(n)

    # Base case: if number is already a single digit
    if n < 10:
        return n

    # Recursive case: sum digits and call again
    digit_sum = sum(int(d) for d in str(n))
    return sum_to_single_digit(digit_sum)


# Testing the function
num = int(input("Enter a number: "))
print("Final single-digit sum:", sum_to_single_digit(num))
