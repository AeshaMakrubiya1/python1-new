'''
Develop a program where a UDF accepts *args and filter out the strings from the arguments.
- Return a tuple of filtered values (e.g., strings in one tuple, numbers in another).
'''

def filter_values(*args):
    strings = []
    numbers = []

    for item in args:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)

    return tuple(strings), tuple(numbers)


# Example usage
str_tuple, num_tuple = filter_values("Aesha", 10, "Hello", 5.5, 20, "Python")
print("Strings Tuple:", str_tuple)
print("Numbers Tuple:", num_tuple)