age1=int(input("enter a age1"))
age2=int(input("enter a age2"))
age3=int(input("enter a age3"))
if age1>age2 and age1>age3:
    print("oldest is",age1)
elif age2>age1 and age2>age3:
    print("oldest is",age2)
elif age3>age1 and age3>age2:
    print("oldest is",age3)
else:
    print("youngest")
