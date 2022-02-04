marks=int(input("enter a marks"))
if marks<25:
    print("F Gade")
elif marks>=25 and marks<=45:
    print("E Grade")
elif marks>=45 and marks<=50:
    print("D Grade")
elif marks>=50 and marks<=60:
    print("C Grade")
elif marks>=60 and marks<=80:
    print("B Grade")
elif marks>80:
    print("A Grade")
else:
    print("marks")