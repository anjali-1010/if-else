month=input("enter a month")
day=int(input("enter a day"))
if month in ("january","fabruary","march"):
    season="winter"
elif month in ("january","fabruary","march"):
    season="winter"
elif month in ("April","may","jun"):
    season="summer"
elif month in ("july","august","september"):
    season="spring"
else:
    print("outumn")
if month=="march" and day>19:
    season="spring"
elif month=="jun" and day>20:
    season="summer"
elif month=="september" and day>21:
    season="outumn"
elif month=="december" and day>20:
    print("season is",season)
