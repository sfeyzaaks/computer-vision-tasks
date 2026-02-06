import cv2
import numpy as np
import os

# OpenCV'nin yüklü olduğu yerdeki hazır XML dosyasını bulur
xml_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' #koordinatlar saklıdır
face_classifier = cv2.CascadeClassifier(xml_path) #verilen görüntünün içindeki belirlenen nesneyi ara

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE) #yüz tanıma fonksiyonu
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2) #verilen koordinatlara dörtgen çizilir
    cv2.imshow("yüz tanıma", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #q ya basılınca görüntü kapanır
        break
cap.release()
cv2.destroyAllWindows()