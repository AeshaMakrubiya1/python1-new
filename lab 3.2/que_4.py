# write a python program using a 'switch-case' equivalent to:
# - take an operator('+', '-', '*', '/')as input.
# - perform the corresponding operation on two numbers entered by the user.

a = float(input("Enter first value : "))
b = float(input("Enter second value : "))
operator = input("enter operators(+, -, *, /) : ")

match operator:
    case '+' :
        print("result:", a + b)
    case '-' :
        print("result:", a - b)
    case '*' :
        print("result:", a * b)
    case '/':
        if num2 !=0:
            print("result:", a / b)
        else:
            print("Error: Division by zero!")
    case _:
        print("Invalid operator!!")