amount=int(input("enter a number"))
if amount>=500:
    note_500=amount//500
    print("500 =",note_500)
if amount>=200:
    note_200=amount//200
    print("200 =",note_200)
if amount>=100:
    note_100=amount//100
    print("100 =",note_100)
if amount>=50:
    note_50=amount//50
    print("50 =",note_50)
if amount>=20:
    note_20=amount//20
    print("20 =",note_20)
if amount>=10:
    note_10=amount//10
    print("10 =",note_10)
if amount>=5:
    note_5=amount//5
    print("5 =",note_5)
else:
    print(amount)
