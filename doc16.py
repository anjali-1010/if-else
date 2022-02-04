side1=int(input("enter a side1"))
side2=int(input("enter a side2"))
side3=int(input("enter a side3"))
if side1+side2>side3:
    print("trigle is valid")
elif side3+side1>side2:
    print("tringle is valid")
elif side3+side3>side1:
    print("tringle is valid")
else:
    print("tringle is not valid")
