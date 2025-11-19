'''
write a python function that accept an arbitrary number of integer arguments and returns their sum and product.
'''

def sum_and_product(*numbers):
    total_sum = 0
    total_product = 1

    for n in numbers:
        total_sum += n
        total_product *= n

    return total_sum, total_product


# Example usage
s, p = sum_and_product(2, 3, 4, 5)
print("Sum:", s)
print("Product:", p)
