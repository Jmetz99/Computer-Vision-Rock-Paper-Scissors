import numpy as np
from keras.models import load_model
import cv2
import time
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
TIMER = int(2)
options = ("Rock", "Paper", "Scissors")
computer_wins = 0
user_wins = 0

def get_user_choice(prediction):
    userchoice = ""
    maxindex = np.argmax(prediction)
    if maxindex == 0: userchoice = "Rock" 
    if maxindex == 1: userchoice = "Paper"
    if maxindex == 2: userchoice = "Scissors"
    return userchoice

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

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

while computer_wins != 3 and user_wins != 3:
    while True:
        ret, img = cap.read()
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "Press q to play", (200, 250), font, 3, (0, 255, 255), 4, cv2.LINE_AA)
        cv2.imshow('Rock-Paper-Scissors', img)
        k = cv2.waitKey(20000)
        if k == ord('q'):
            prev = time.time()
            
            while TIMER >= 0:
                ret, img = cap.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(TIMER + 1), (200, 250), font, 7, (0, 255, 255), 4, cv2.LINE_AA)
                cv2.imshow('Rock-Paper-Scissors', img)
                cv2.waitKey(200)
                cur = time.time()
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
            else:
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data)
                cv2.imshow('You chose', frame)
                user_choice = get_user_choice(prediction)
                computer_choice = get_computer_choice()
                wins = get_winner(computer_choice, user_choice)
                TIMER = 2
                if wins == "user": 
                    user_wins += 1
                    print("You won that one")
                if wins == "computer":
                    computer_wins +=1
                    print("The computer won that one")
                else:
                    print("It's a Draw")
                break


cap.release()
cv2.destroyAllWindows()

if computer_wins == 3:
    print("The computer won!")

if user_wins == 3:
    print("You won!")