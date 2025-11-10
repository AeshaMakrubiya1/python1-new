# write a program in python to find the maximum number from the given three numbers using a nested if statements.

a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
c = int(input("Enter third value : "))

if a==b and b==c:
    print("All are same")
else:
    if a>b:
        if a>c:
            print("a is max")
        else:
            print("c is max")
    else:
        if b>c:
            print("b is max") 
        else:
            print("c is max")       
    
 