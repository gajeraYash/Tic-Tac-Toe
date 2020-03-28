from func import *

from random import randint,getrandbits
print('Welcome to Tic Tac Toe!')

goesFirst = bool(getrandbits(1))

print("Player {} goes first!".format(int(goesFirst)+1))
if goesFirst == False:
    player1,player2 = selectMarker()
else:
    player2,player1 = selectMarker()
clear()
print(f"Player 1 : {player1}\nPlayer 2 : {player2}\n")
engine(goesFirst,player1,player2)



