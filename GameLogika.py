import random
number = random.randint(1, 25)
chances = 0
print("Guess a number (between 1 and 25")
while chances < 5:
    guess = int(input("Enter Your Guess : "))
    if guess == number:
        print("Congratulations YOU WON")
        exit()
    elif guess < number:
        print("Your Guess was to low")
    else:
        print("Your Guess was to high")
    chances += 1
    print("Chance Left : ",5-chances)

print("YOU LOSE!!! The number is : ", number)