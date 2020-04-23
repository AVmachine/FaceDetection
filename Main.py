import numpy as np
import cv2
import random

cap = cv2.VideoCapture(2)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    tracker = 0
    color1 = 255
    color2 = 0
    color3 = 0
    for (x, y, w, h) in faces:
        tracker += 1
        color1 -= 60
        color2 += 25
        color3 += 35
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (color1, color2, color3), 5)

        #Text for face order numbers
        text = cv2.putText(frame, "Face ID: " + str(tracker), (x, y),
                    cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 5)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
