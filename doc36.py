price=int(input("enter tha price of like"))
if price>100000:
    tax=15/100*price
    price(tax)
elif price>50000 and price<=100000:
    tax=10/100*price
    print(tax)
elif price<=500000:
    tax=5/100*price
    print(tax)
else:
    print(price)