import os
import random
#Rock Paper Scissor Game made by Priyam


print("Welcome to Rock Paper Scissor")
def game(comp,player2):
    if comp==player2:
          print("Game tie")
    elif comp=="R":
        if player2=="S":
            print("You Win")
        elif player2=="P":
                print("You Lost")
    elif comp=="P":
        if player2=="S":
            print("You Win")
        elif player2=="R":
                print("You Lost")
    elif comp=="S":
        if player2=="R":
            print("You Win")
        elif player2=="P":
                print("You Lost")


player1=random.randint(1,3)
if player1==1:
     comp="R"
elif player1==2:
     comp="P"
elif player1==3:
     comp="S"


while(True):
    you=input("Player turn: Enter Rock(R), Paper(P) or Scissors(S)? :")
    player2=you.upper()
    while(True):
        if player2 in ("S","R","P"):
            break
        else:
            print("Please enter right key.")
            you=input("Player turn: Enter Rock(R), Paper(P) or Scissors(S)? :")
            player2=you.upper()
    game(comp,player2)
    print(f"Computer choice : {comp}")
    print(f"Yo choice : {player2}")
    again=input("Enter E for exit OR Enter for play Again : ")
    rg=again.upper()
    if rg=="E":
        break

