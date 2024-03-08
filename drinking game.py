import random
drinks = ("vodka", "tequila", "rum", "whiskey", "arak", "whiskey", "pisco")
try:
    name = input("What is your name? ")
    age = input("How old are you? ")
    age = int(age) #convert string to integer
    country = input("Where are you from?")
except ValueError:
    print("Invalid age. Please enter a number. ")
else:
    if age < 0 or age > 140:
        print("you are not human. this game is for humans only.")
    elif age>120:
        print("you are too old to play this awesome drinking game")
    # now we have a good age to play with
    elif age <18:
        print("You are a minor. You cannot play the awesome drinking game. ")
    elif country == "USA" or country == "UAE" and age < 21:
        print("You are not allowed to drink in USA or UAE. You cannot play this awesome drinking game")
    else:
        print("You are an adult. You can play the awesome drinking game. ")
        print("Have some", random.choice(drinks), "and enjoy the game.")
