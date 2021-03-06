import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    faces = face_cascade.detectMultiScale(
        img,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('Deteccion de rostro',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # 'ESC' para salir
        break

cap.release()
cv2.destroyAllWindows()
