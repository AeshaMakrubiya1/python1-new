# write a program in python to find the maximum number from the given four numbers using a nested if statements.

a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
c = int(input("Enter third value : "))
d = int(input("Enter fourth value : "))

if a > b:
    if a > c:
        if a > d:
            print("a is max")
        else:
            print("d is max")
    elif c > d:
        print("c is max")
    else:
        print("d is max")
else:
    if b > c:
        if b > d:
            print("b is max")
        else:
            print("d is max")
    elif c > d:
        print("c is max")
    else:
        print("d is max")