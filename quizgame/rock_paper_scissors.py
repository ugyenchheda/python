import random

user_wins = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, paper, scissors or type Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock : 0, paper: 1, scissors: 2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick =="scissors":
        print("You Won!")
        user_wins += 1
    
    elif user_wins== "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_wins == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
    
    else:
        print("You Lost")
        computer_win += 1

print("You won", user_wins, "times.")
print("The computer won", computer_win, "times.")
print("Goodbye!")