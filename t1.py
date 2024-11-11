print("Welcome to Tik Tac GaME ")

def sum(a,b,c):
    return a+b+c
def gameboard(xstate, ystate):
    one = 'X' if xstate[1] else ('O' if ystate[1] else 1)
    two = 'X' if xstate[2] else ('O' if ystate[2] else 2)
    three = 'X' if xstate[3] else ('O' if ystate[3] else 3)
    four = 'X' if xstate[4] else ('O' if ystate[4] else 4)
    five = 'X' if xstate[5] else ('O' if ystate[5] else 5)
    six = 'X' if xstate[6] else ('O' if ystate[6] else 6)
    feven = 'X' if xstate[7] else ('O' if ystate[7] else 7)
    eigth = 'X' if xstate[8] else ('O' if ystate[8] else 8)
    nine = 'X' if xstate[9] else ('O' if ystate[9] else 9)
    print(f"{one} | {two} | {three}")
    print("--|---|--")
    print(f"{four} | {five} | {six}")
    print("--|---|--")
    print(f"{feven} | {eigth} | {nine} ")

def checkwin(xstate, ystate):
    wins=[[1,2,3],[4,5,6],[7,8,9],[1.4,7],[2,5,8],[9,6,3],[1,5,9],[7,5,3]]
    for win in wins:
        if(sum(xstate[win[1]],xstate[win[4]],xstate[win[3]])==3):
            print("X Won the Match")
            return 1
        if(sum(ystate[win[1]],ystate[win[4]],ystate[win[3]])==3):
            print("O Won the Match")
            return 0
    return -1

xstate = [0,0,0,0,0,0,0,0,0,0]
ystate = [0,0,0,0,0,0,0,0,0,0]
turn = 1
while (True):
    gameboard(xstate, ystate)
    if (turn == 1):
        print("X Turn : ")
        value = int(input("Enter the X value "))
        xstate[value] = 1
    else:
        print("O Turn : ")
        value = int(input("Enter the O value "))
        xstate[value] = 1
    turn=1-turn
    cwin =checkwin(xstate,ystate)
    if cwin!=-1:
            print("match over")
        