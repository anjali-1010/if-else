day=int(input("enter a days number"))
if day<=5:
    amt1=day*2
    print(amt1)
elif day<6 and day<10:
    amt2=day*3
    print(amt2)
elif day<10 and day<15:
    amt3=day*4
    print(amt3)
elif day>15:
    amt4=day*5
    print(amt4)
# else:
    # print(day)
