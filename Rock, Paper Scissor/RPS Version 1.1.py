# author: Siddhant Shah
# Desc: An update to basic version of RPS. This program converts inout text to upper case and does all testing
# using upper case. This removes any ambiguity about lower and upper case

import random

print("Welcome to the Rock, Paper, Scissors Game")
user_input = input("Please choose one of the 3 options, 'Rock', 'Paper' or 'Scissor': ").upper()

print()

game_tuple = ('Rock', 'Paper', 'Scissor')   # tuple which holds all possible option of game

# using randint function of class random to choose one of 3 items in tuple and converting to uppercase
random_choice = game_tuple[random.randint(0, 2)].upper()
print(f"You choose: {user_input}")
print(f"Computer choose: {random_choice}")

# creating constants. These are not mandatory but I am using them to make code look cleaner
ROCK = "rock".upper()
PAPER = "paper".upper()
SCISSOR = "Scissor".upper()

print()

# checking different conditions
if user_input == ROCK:
    if random_choice == ROCK:         # if both user and computer have selected 'Rock'
        print("IT A DRAW!!!")
    elif random_choice == PAPER:      # if user have selected 'Rock' but computer has selected 'Paper'
        print("LOL!! YOU LOST")
    elif random_choice == SCISSOR:    # if user have selected 'Rock' but computer has selected 'Scissor'
        print("YAY!! YOU WIN")
elif user_input == PAPER:
    if random_choice == ROCK:         # if user have selected 'Paper' but computer has selected 'Rock'
        print("LOL!! YOU LOST")
    elif random_choice == PAPER:      # if both user and computer have selected 'Paper'
        print("IT A DRAW!!!")
    elif random_choice == SCISSOR:    # if user have selected 'Paper' but computer has selected 'Scissor'
        print("YAY!! YOU WIN")
elif user_input == SCISSOR:
    if random_choice == ROCK:         # if user have selected 'Scissor' but computer has selected 'Rock'
        print("YAY!! YOU WIN")
    elif random_choice == PAPER:      # if user have selected 'Scissor' but computer has selected 'Paper'
        print("LOL!! YOU LOST")
    elif random_choice == SCISSOR:    # if both user and computer have selected 'Scissor'
        print("IT A DRAW!!!")
else:
    print("Please enter valid input")
