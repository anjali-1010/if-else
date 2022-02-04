num1=int(input("emter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if num1<num2 and num2<num3:
    print(num1,"num1 is small")
elif num2<num1 and num2<num3:
    print(num2,"num2 is small")
# elif num3>num1 and num2>num3:
#     print(num3,"num3 is small")
else:
    print(num3,"num3 is small")
