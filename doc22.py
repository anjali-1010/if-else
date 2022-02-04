quantity=int(input("enter a number"))
if (quantity*100>1000):
    total_cost=(quantity*100)-(10*(quantity*100)/100)
    print(total_cost)
else:
    print("total_cost =",quantity*100)
