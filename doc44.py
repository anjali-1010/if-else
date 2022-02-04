age=int(input("enter a age"))
sex=input("enter a F & M")
N_D=int(input("enter a number a days"))
if (age>30 or age<80)  and sex=="m":
    amt=N_D*700
    print(amt)
elif age>=30 and age<80 and sex=="f":
    amt=N_D*750
    print(amt)

elif age>30 and age<40 and sex=="m":
    amt=N_D*880
    print(amt)
elif age>30 and age<40 and sex=="f":
    amt=N_D*850
    print(amt)
else:
    print(age,sex,N_D)