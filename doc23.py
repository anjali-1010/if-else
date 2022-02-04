salary=int(input("enter a number"))
Y_O_S=int(input("enter a year of sarvice"))
if (Y_O_S>=5):
    bonus=salary+(salary*Y_O_S*5)/100
    print(bonus)
else:
    print("N0 bonus")