from numpy import random
import time
score_com = 0
score_pla = 0
element = True
while element:
    computer = random.choice(('r','p','s'))
    player = input("rock,paper,scissor:")
    if computer=="r" and player=="r":
        print("No Result")
    elif computer=="r" and player=="p":
        print("Player wins")
        score_pla += 1
    elif computer=="r" and player=="s":
        print("Computer wins")
        score_com += 1
    elif computer=="p" and player=="r":
        print("Computer wins")
        score_com += 1
    elif computer=="p" and player=="p":
        print("No result")
    elif computer=="p" and player=="s":
        print("Player wins")
        score_pla += 1
    elif computer=="s" and player=="r":
        print("Player wins")
        score_pla += 1
    elif computer=="s" and player=="p":
        print("Computer wins")
        score_com += 1
    else:
        print("No Result")
    if score_com==5:
        element = False
        print("Computer is the Winner of Today's Battle")
        time.sleep(10)
    elif score_pla==5:
        element = False
        print("---------------------------------------")
        print("GAME OVER")
        print("Player is the Winner of Today's Battle")
        time.sleep(10)
        
