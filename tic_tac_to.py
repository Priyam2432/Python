a=['0','1','2','3','4','5','6','7','8','9']

def board():
    print("|",a[1],"|",a[2],"|",a[3],"|")
    print("-------------")
    print("|",a[4],"|",a[5],"|",a[6],"|")
    print("-------------")
    print("|",a[7],"|",a[8],"|",a[9],"|")
    print("-------------")
board()
for i in range(5): 
    player1=int(input("Player 1 enter your  choice : "))
    a[player1]='X'
    board()
    player2=int(input("Player 2 enter your  choice : "))
    a[player2]='0'
    board()
    