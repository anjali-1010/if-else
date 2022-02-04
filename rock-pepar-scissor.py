player1=input("enter a player1 sign")
player2=input("enter a player2 sign")
if player1=="rock" and player2=="scissor" or player1=="pepar" and player2=="rock" or player1=="secissor" and player2=="pepar":
    print("player1 is winner")
elif player1=="secissor" and player2=="rock" or player1=="rock" and player2=="pepar" or player1=="pepar" and player2=="secissor":
    print(" player2 is winner")
else:
    print("drow")
