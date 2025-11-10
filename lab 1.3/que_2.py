# write a program where the user inputs a floating-point number.
#  - Convert this number into an integer using int() and print both values with a meassage explaining the difference.

num = float(input("Enter a floating point numberv : "))
int_num = int(num)

print("Original number:", num)
print("After conversion to int:", int_num)
print("Note: int() removes the decimal part.")