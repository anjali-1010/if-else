salary=int(input("enter a salary"))
if salary<=10000:
    DA=salary*0.8
    HRA=salary*0.2
    print("gross =",salary+DA+HRA)
elif salary<=20000:
    DA=salary*0.9
    HRA=salary*0.25
    print("gross =",salary+DA+HRA)
elif salary>20000:
    DA=salary*0.95
    HRA=salary*0.30
    print("gross =",salary+DA+HRA)
else:
    {salary}
    