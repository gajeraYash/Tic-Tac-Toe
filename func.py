
from os import system

currentGame = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
gameRound = 1

def clear():
    system('clear')
    print("TIC TAC TOE")

def selectMarker():
    u1 = None
    while True:
        if u1 == None:
            u1 = input('Select A Marker X or O:  ').upper()
        elif u1 != 'X' and u1 != 'O':
            print('Invalid Input!')
            u1 = input('Select A Marker X or O:  ').upper()
        elif u1 == 'X':
            u2 = 'O'
            break
        else:
            u2 = 'X'
            break
    return u1, u2

def display_board(board):
    print(f"-----------\n GAME : {board[0]}\n-----------")
    print(f" {board[7]} | {board[8]} | {board[9]} \n-----------\n {board[4]} | {board[5]} | {board[6]} \n-----------\n {board[1]} | {board[2]} | {board[3]} \n")


def instructions():
    instruc = ('Ex','1','2','3','4','5','6','7','8','9')
    print("Please use your number keypad to input the location in the board")
    print("Here is an example of positions on board")
    display_board(instruc)

def playerInput():
    while True:
        x = input()
        try:
            if 0<int(x)<10:
                if currentGame[int(x)] == ' ':
                   return int(x)
                else:
                    print("Position Already Taken!")
            else:
                print("Input a integer between 1-9")
        except ValueError:
            print("Input a valid integer.")
def winCheck(c):
    winPat = [(7,8,9),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1)]
    for i in winPat:
        if (c== currentGame[i[0]]) and (c== currentGame[i[1]]) and (c== currentGame[i[2]]):
            return True
        else:
            continue
    return False

def checkBoard():
    if ' ' not in currentGame:
        return True
    else:
        return False

def reset():
    for i in range (1,10):
        currentGame[i] = ' '
    global gameRound
    gameRound += 1
    currentGame[0] = gameRound

def engine(fp,p1,p2):
    currentGame[0] = gameRound
    while True:
        if fp == False:
            c = p1
        else:
            c = p2
        display_board(currentGame)
        print(f"{c} Position: ")
        currentGame[playerInput()] = c
        if winCheck(c) == True:
            display_board(currentGame)
            print(f"Player {int(fp)+1}  WON!")
            break
        elif checkBoard():
            reset()
        else:
            fp = not fp
            clear()
        