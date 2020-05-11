import cv2
import os
import glob
import numpy as np
import random
from os.path import isfile, join
import time


#####MAIN######
#For creating video from images
# import glob
#
# img_array = []
#
#
# for filename in sorted(glob.glob('P2E_S5_C1.1/*.jpg')):
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)
#
# out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 7, size)
#
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()

#Where video is read from
cap = cv2.VideoCapture('project.avi')  # for a video
# cap = cv2.VideoCapture(2) #For a webcam, replace with 0 or 1 for main webcam

# Haar Cascade algorithm
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.5, 5)

    tracker = 0
    color1 = 255
    color2 = 0
    color3 = 0
    for (x, y, w, h) in faces:
        tracker += 1
        color1 -= 60
        color2 += 25
        color3 += 35
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (color1, color2, color3), 4)

        # Text for face order numbers
        text = cv2.putText(frame, "Face ID: " + str(tracker), (x, y),
                           cv2.FONT_HERSHEY_TRIPLEX, .5, (255, 255, 255), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
    time.sleep(.05)
    cv2.imshow('frame', frame)
    cv2.waitKey(2)