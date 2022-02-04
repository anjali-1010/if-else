num1=int(input("enter a Physics number"))
num2=int(input("enter a Chemistry number"))
num3=int(input("enter a Biology number"))
num4=int(input("enter a Methemetic number"))
num5=int(input("enter a Computer number"))
per=(num1+num2+num3+num4+num5)*100//500
if per>=90:
    print("Grade A")
elif per>=80:
    print("Grade B")
elif per>=70:
    print("Grade C")
elif per>=60:
    print("Grade D")
elif per>=40:
    print("Grade E")
elif per<=40:
    print("Grade F")
else:
    print("Fail")
