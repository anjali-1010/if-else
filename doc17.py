side1=int(input("enter a side1="))
side2=int(input("enter a side2="))
side3=int(input("enter a side3="))
if side1==side2==side3:
    print("equlaterad")
elif side1==side2>=side3:
    print("isoplate")
else:
    print("scalence")