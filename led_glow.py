import cv2
import mediapipe as mp
from cvzone.SerialModule import SerialObject


arduino = SerialObject('COM3') 


mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)


cap = cv2.VideoCapture(0)

def count_fingers_up(handLms):
    fingers_up = 0
    tip_ids = [4, 8, 12, 16, 20]
    for tip_id in tip_ids:
        x, y = handLms.landmark[tip_id].x, handLms.landmark[tip_id].y
        x_base, y_base = handLms.landmark[tip_id - 2].x, handLms.landmark[tip_id - 2].y
        if y < y_base:
            fingers_up += 1
    return fingers_up

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            fingers_up = count_fingers_up(handLms)

            
            arduino.sendData([fingers_up])

    cv2.imshow("Image", img)
    cv2.waitKey(1)