num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if num1>num2:
    if num1>num3:
        median=num1
    elif num2>num3:
        median=num2
    else:
        median=num3
else:
    if num1>num3:
        median=num1
    elif num2<num3:
        median=num2
    else:
        median=num3
    print("The mdian is",median)
