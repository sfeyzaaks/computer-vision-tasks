import cv2
import numpy as np

cap = cv2.VideoCapture(0) #kamerayı başlatır

while True:
    
    ret, frame = cap.read() #kameradan kareler okunur
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #görüntüyü hsv renk uzayına çevirdik

    
    lower_black = np.array([0, 0, 0]) #siyah renk için alt sınırlar
    upper_black = np.array([180, 255, 50]) #siyah renk için üst sınırlar

    
    mask = cv2.inRange(hsv, lower_black, upper_black)#siyah bölgeler beyaz diğer yerler siyah yapılarak maskeleme yapılır

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #nesnenin etrafını çizmek için konturleri bul

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500: 
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Siyah Nesne", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 7. Sonuçları ekrana bas
    cv2.imshow("Kamera", frame)
    cv2.imshow("Maske (Siyah Alanlar)", mask)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()