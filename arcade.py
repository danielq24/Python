'''
The class uses two functions that is activated on user input
to run either the dice roll or rock paper scissors.
The program continue if the user inputs y at the end of
each game
'''

import random
play = "y"

def dice_roll():  #function for dice roll
    number = random.randint(1, 6)
    print(number)

def rps(): #function for rock,paper,scissors
    choice = ["rock", "paper", "scissor"]
    cpu_choice = random.choice(choice)
    user_choice = input("rock, paper, scissor \n")
    if user_choice == cpu_choice:
        print("tie, CPU chose " + cpu_choice)
    if user_choice == "rock":
        if cpu_choice == "paper":
            print("you lose, CPU chose " + cpu_choice)
        if cpu_choice == "scissor":
            print("you win, CPU chose " + cpu_choice)
    if user_choice == "paper":
        if cpu_choice == "scissor":
            print("you lose, CPU chose " + cpu_choice)
        if cpu_choice == "rock":
            print("you win, CPU chose " + cpu_choice)
    if user_choice == "scissor":
        if cpu_choice == "rock":
            print("you lose, CPU chose " + cpu_choice)
        if cpu_choice == "paper":
            print("you win, CPU chose " + cpu_choice)


while play == "y": #asks user what game to play and to continue
    user_choice = input("dice roll or rps (rock, paper, scissors)?\n")
    if user_choice == "dice roll":
        dice_roll()
    if user_choice == "rps":
        rps()
    play = input("Would you like to continue? Press y to proceed. \n")

