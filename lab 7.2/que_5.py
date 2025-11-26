'''
create a recursive function to print all prime numbers between two given numbers.
'''
# Function to check if a number is prime (recursively)
def is_prime(n, i=2):
    # Handle numbers less than 2
    if n < 2:
        return False

    # If i*i > n, no divisor found → it's prime
    if i * i > n:
        return True

    # If divisible → not prime
    if n % i == 0:
        return False

    # Recursive call with next divisor
    return is_prime(n, i + 1)


# Function to print primes in a range (recursively)
def print_primes(start, end):
    # Base case: when range is finished
    if start > end:
        return

    # Print if prime
    if is_prime(start):
        print(start)

    # Recursive call for next number
    print_primes(start + 1, end)


# Testing the function
a = int(input("Enter start number: "))
b = int(input("Enter end number: "))

print(f"Prime numbers between {a} and {b}:")
print_primes(a, b)
