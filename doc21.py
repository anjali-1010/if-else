unit=int(input("enter a electricity bill"))
if unit<=50:
    amt=unit*25
    sc=amt*(20/100)
    total_sc=amt+sc
    print(total_sc)
elif unit<=150:
    amt=(25+(unit-50)*0.75)
    sc=amt*(20/100)
    total_sc=amt+sc
    print(total_sc)
elif unit<=250:
    amt=100+(unit-150*1.20)
    sc=amt*(20/100)
    total_sc=amt+sc
    print(total_sc)
elif unit<=350:
    amt=170+unit*25
    sc=amt*(20/100)
    total_sc=amt+sc
    print(total_sc)
else:
    print("no change")

