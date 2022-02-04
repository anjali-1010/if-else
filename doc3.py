num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if num1>num2:
    print(num1,"is maximum")
elif num2>num3:
    print(num2,"is maximum")
elif num3>num1:
    print(num3,"is maximum")
else:
    print("all equal")