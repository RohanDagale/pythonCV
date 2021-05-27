import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands() #imgRGB is value given to hands
mpdraw = mp.solutions.drawing_utils
ptime = 0
ctime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1/(ctime - ptime)
    pTime = cTime
    cv2.putText('img', str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,0), 3)
    cv2.imshow('image', img)
    cv2.waitKey(1)