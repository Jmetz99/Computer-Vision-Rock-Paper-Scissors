import numpy as np
from keras.models import load_model
import cv2
import time

TIMER = int(3)
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "Press q to play", (200, 250), font, 3, (0, 255, 255), 4, cv2.LINE_AA)
    cv2.imshow('a', img)
    k = cv2.waitKey(20000)
    if k == ord('q'):
        prev = time.time()
        
        while TIMER >= 0:
            ret, img = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(TIMER), (200, 250), font, 7, (0, 255, 255), 4, cv2.LINE_AA)
            cv2.imshow('a', img)
            cv2.waitKey(200)
            cur = time.time()
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
        else:
            ret, img = cap.read()
            cv2.imshow('a', img)
            cv2.waitKey(1000)
            user_choice = cv2.imwrite('user_choice', img)
            break


resized_frame = cv2.resize(user_choice, (224, 224), interpolation = cv2.INTER_AREA)
image_np = np.array(resized_frame)
normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
data[0] = normalized_image
prediction = model.predict(data)
            

cap.release()
cv2.destroyAllWindows()

def get_prediction():
    maxindex = np.argmax(prediction)
    if maxindex == 0: return "Rock" 
    if maxindex == 1: return "Paper"
    if maxindex == 2: return "Scissors"

user_choice = get_prediction()

print(user_choice)