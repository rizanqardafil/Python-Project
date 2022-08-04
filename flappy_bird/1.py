import random
import os
player = 0
computer = 0

suit=["", "Rock", "Paper", "Scissors"]
history = [0]
player_pick = None
while player_pick != 0:
    player_pick = int(input(">>>"))
    if player_pick == history[-1]:
        break
    else:
        if player_pick != 0:
            history.append(player_pick)
            print(f"Your Choice {suit[player_pick]}")
            computer_pick = random.randint(1,3)
            print(f"Opponent Choice {suit[computer_pick]}")
            
            if player_pick == computer_pick:
                print("Draw")
            else:
                if(player_pick == 1 and computer_pick == 2) or (player_pick==2 and computer_pick == 3) or (player_pick == 3 and computer_pick == 1):
                    print("You Win")

                else:
                    print("You Lose, Try Again")                    
            input("Enter>>")
print(history)