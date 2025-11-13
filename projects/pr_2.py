print("Hello! Welcome To The Pattern Generator and Number Analyzer. ")

while True:
    print("\nOption : 1.pattern 2.NumberCheck 3.End")
    select = input("Enter option:")
    
    if select == "1":
        a = int(input("How Many Rows?"))
        if a <=0:
            print("break on wrong input")
            break
        for i in range(1,a+1):
            for j in range(i):
                print("*"*i)
            print()
    elif select == "2":
        stt = int(input("Enter Your Starting Range : "))
        enn = int(input("Enter Your Ending Range :"))
        if stt >= enn:
            print("Invalid input -> continue")
            continue
        add = 0
        for num in range(stt, enn+1):
            if num % 2 == 0:
                print(num, "even")
            else:
                print(num, "odd")
            add += num
        print("Sum =", add)
    elif select == "3":
        print("End program")
        break
    else:
        print("Try again")