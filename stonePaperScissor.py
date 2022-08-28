import random
from scipy import rand
print("HELLO THERE,\nTHIS IS STONE-PAPER-SCISSOR GAME.\nLets Play It!")
def game(comp,player):
    if comp == 'S' and player == 'P':
        print("YOU WIN!")
    elif comp == 'P' and player == 'S':
        print("YOU LOSE!")
        
    if comp == 'S' and player == 'SC':
        print("YOU LOSE!")
    elif comp == 'SC' and player == 'S':
        print("YOU WIN!")
        
    if comp == 'SC' and player == 'P':
        print("YOU LOSE!")
    elif comp == 'P' and player == 'SC':
        print("YOU WIN!")
        
    if comp == 'S' and player == 'S':
        print("GAME TIE!")
    elif comp == 'P' and player == 'P':
        print("GAME TIE!")
    elif comp == 'SC' and player == 'SC':
        print("GAME TIE!")
        
print("COMPUTER'S TURN:\nSELECT STONE(S) PAPER(P) OR SCISSOR(SC):")
a = random.randint(1,3)
print("COMPUTER HAVE SELECTED.")
player = input("NOW PLAYER'S TURN:\nSELECT STONE(S) PAPER(P) OR SCISSOR(SC):")

if a == 1:
    comp = 'S'
elif a == 2:
    comp = 'P'
elif a == 3:
    comp = 'SC'

print(f"COMPUTER CHOSE: {comp}")
print(f"YOU CHOSE: {player}")

b = game(comp,player)