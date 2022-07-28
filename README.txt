Computer Vision Rock Paper Scissors

This project takes a model from the "Teachable Machine" website on line which has been trained with images I generated from my webcam. 

## Milestone 1

- Downloaded a model generated from the "Teachable Machine" website which has been trained with images of me showing the three options rock, paper or scissors generated from my webcam. I pushed these changes to my first Git repo.

## Milestone 2

Created my first conda environment in which I downloaded the required dependencies to run the teachable machine model. Saved in requirement.txt file on Git repo.

## Milestone 3

Created a file called manual_rps.py which contains the code to play rock, paper scissors with the computer. The code is given below.


```python
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
```
## Milestone 4
Incorporating the model downloaded from teachable machine, the user can now input their choice of Rock-Paper-Scissors by showing it to the camera after a countdown.
The game is played three times before a winner is determined.

## Conclusions

