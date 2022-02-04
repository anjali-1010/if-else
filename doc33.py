unit=int(input("enter a number"))
if unit<=100:
    amt=unit*0
    print("no change")
elif unit<=200:
    amt=0+(unit-100)*5
    print(amt)
elif unit<=400:
    amt=500+(unit-200)*10
    print(amt)
else:
    print(unit)
    