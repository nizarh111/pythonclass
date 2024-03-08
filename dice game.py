import random
# play a dice game with 3 lives, 6 wins the game
lives = 3
while lives > 0:
    print("You have,", lives, "lives left.")
    #roll the dice
    dice = random.randint(1,6)
    print("You rolled a", dice)
    #check if you win
    if dice == 6:
        print("\n\nYOU WIN!\n\n")
        break
    else:
        lives = lives - 1

    print("Thank you for playing. Goodbye.")
