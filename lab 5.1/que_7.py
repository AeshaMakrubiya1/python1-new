'''
check if a string starts with "Hello" and ends with "world".
- remove all non-alphabetic characters from "data123#Science!".
-reverse the string "python"
'''

s = "Hello world"

print("Starts with Hello:", s.startswith("Hello"))
print("Ends with World:", s.endswith("World"))

# Remove non-alphabet characters
import re
clean = re.sub("[^A-Za-z]", "", "Data123#Science!")
print(clean)

# Reverse string
print("nohtyP"[::-1])

