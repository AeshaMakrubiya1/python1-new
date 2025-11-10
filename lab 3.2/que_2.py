# write a program in python to find the minimum number from the given three numbers using a nested if statements.

a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
c = int(input("Enter third value : "))

if a==b and b==c:
    print("All are same")
else:
    if a<b:
        if a<c:
            print("a is minimum")
        else:
            print("c is minimum")
    else:
        if b<c:
            print("b is minimum") 
        else:
            print("c is minimum")       
    