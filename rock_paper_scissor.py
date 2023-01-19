"""
Purpose: Create a rock, paper, scissor game using while loops
and if statements. The program will run one iteration and
prompt the user to input y to play the game again or quit.
"""
import random
proceed = "y"

while proceed == "y":
    choice = ["rock", "paper", "scissor"]
    cpu_choice = random.choice(choice)
    user_choice = input("rock, paper, scissor \n")
    if user_choice == cpu_choice:
        print("tie, CPU chose " +  cpu_choice)
    if user_choice == "rock":
        if cpu_choice == "paper":
            print("you lose, CPU chose " +  cpu_choice)
        if cpu_choice == "scissor":
            print("you win, CPU chose " +  cpu_choice)
    if user_choice == "paper":
        if cpu_choice == "scissor":
            print("you lose, CPU chose " +  cpu_choice)
        if cpu_choice == "rock":
            print("you win, CPU chose " +  cpu_choice)
    if user_choice == "scissor":
        if cpu_choice == "rock":
            print("you lose, CPU chose " +  cpu_choice)
        if cpu_choice == "paper":
            print("you win, CPU chose " +  cpu_choice)
    proceed = input("Would you like to continue? Press y to proceed. \n") #user inputs y to continue & no to stop
