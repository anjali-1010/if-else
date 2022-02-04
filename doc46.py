text=input("enter a input")
if text>="1" and text<="9":
    print("integer")
elif text>="A" and text<="Z" or text>="a" and text<="z":
    print("string")
else:
    print("special character")