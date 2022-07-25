import random

options = ("Rock", "Paper", "Scissors")

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice


def get_user_choice():
    user_choice = input("Enter your choice of Rock, Paper or Scissors: " )
    return user_choice


def get_winner(computer_choice, user_choice):
    winner = ""
    if computer_choice == "Paper" and user_choice == "Rock":
        winner = "computer"
    elif computer_choice == "Paper" and user_choice == "Scissors":
        winner = "user"
    elif computer_choice == "Rock" and user_choice == "Paper":
        winner = "user"
    elif computer_choice == "Rock" and user_choice == "Scissors":
        winner = "computer"
    elif computer_choice == "Scissors" and user_choice == "Paper":
        winner = "computer"
    elif computer_choice == "Scissors" and user_choice == "Rock":
        winner = "user"
    else:
        winner = "Draw"
    return winner
    

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)
    if winner == "Draw": 
        print(winner) 
    else:
        print("The winner is the", winner)

play()