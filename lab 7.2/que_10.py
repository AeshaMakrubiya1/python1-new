'''
write a program where a global variable is updated  inside a function to keep track of the sum of all numbers entered by the user
'''

total_sum = 0   # Global variable

def add_number(n):
    global total_sum   # Allow modification of global variable
    total_sum += n     # Update the global sum


# Taking multiple inputs from the user
count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    add_number(num)

print("Total sum of all numbers entered:", total_sum)
