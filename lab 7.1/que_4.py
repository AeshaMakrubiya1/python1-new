'''
write a UDF that takes a string as input and returns the frequency of each character in the string as a dictionary
'''

def char_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage:
input_string = "hello world"
result = char_frequency(input_string)

print("Character frequencies:", result)
