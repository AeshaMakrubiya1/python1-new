'''
create a list and a tuple both containing the same 3 item.
- Try changing the first item of each.
- Discuss the error (in case of tuple) and explain why it happens.
'''

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0] = 100
print("Updated list:", my_list)

try:
    my_tuple[0] = 100
except TypeError:
    print("Error: Cannot change tuple items (tuple is immutable).")