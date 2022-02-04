cost_price=int(input("enter a number"))
salling_price=int(input("enter a number"))
if cost_price<salling_price:
    cost_price-salling_price
    print("profit hoga")
elif cost_price>salling_price:
    salling_price-cost_price
    print("loss hoga")
else:
    print("no profit,no loss")