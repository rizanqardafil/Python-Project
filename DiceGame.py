from random import randint

roll = "y"
while roll == "y":
    print("Rolling the dices...")
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    print(dice1, dice2)

    roll = input("Roll Again?")