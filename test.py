
#import random
#for i in range(4):
    #print(f'{random.randint(0,1) + 1}--{i}\n')
'''
x = None
b = False
while b != True:
    try:
        x = int(input("PLease :"))
    except ValueError:
        print("Not an integer value...")
    else:
        if (0 < x < 11):
            b = True
        else:
            b =  False
        print(b)
'''
'''while True:
    x = input("HERE: ")
    try:
        if 0<int(x)<11:
            print("YES")
            break
        else:
            print("NO")
    except ValueError:
        print("Please Input Valid Number")

'''
winPat = [(7,8,9),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1)]
playBoard = ('#',' ',' ',' ',' ',' ',' ',' ',' ',' ')
currentGame = ['#','x','x','o','o','o','o','x','x','x']

def display_board(board):
    print(f"-----------\n GAME : {board[0]}\n-----------")
    print(f" {board[7]} | {board[8]} | {board[9]} \n-----------\n {board[4]} | {board[5]} | {board[6]} \n-----------\n {board[1]} | {board[2]} | {board[3]} \n")

display_board(currentGame)
currentGame = None
currentGame = list(playBoard)
display_board(currentGame)
print(type(currentGame))
for i in range(0,10):
    print(i)