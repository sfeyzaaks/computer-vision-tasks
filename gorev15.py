import cv2
import numpy as np

def geri_cagirma(x):
    pass
cap = cv2.VideoCapture(0) #kamera getirilir

cv2.namedWindow("trackbars") #trackbars adında yeni pencere eklenir
cv2.resizeWindow("trackbars", 640, 540) #pencere yeniden boyutlandırılır
cv2.createTrackbar("hue min", "trackbars", 0, 179, geri_cagirma ) #trackbarlar max ve min değerleriyle oluşturulur
cv2.createTrackbar("hue max", "trackbars", 179, 179, geri_cagirma )
cv2.createTrackbar("sat min", "trackbars", 0, 255, geri_cagirma )
cv2.createTrackbar("sat max", "trackbars", 255, 255, geri_cagirma )
cv2.createTrackbar("value min", "trackbars", 0, 255, geri_cagirma )
cv2.createTrackbar( "value max", "trackbars", 255, 255, geri_cagirma )


while True:
    success, img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #hsv formatına dönüştürüldü
    h_min = cv2.getTrackbarPos("hue min", "trackbars") #trackbarlar oluşturulan pencereye eklenir
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    sat_min = cv2.getTrackbarPos("sat min", "trackbars")
    sat_max = cv2.getTrackbarPos("sat max", "trackbars")
    value_min = cv2.getTrackbarPos("value min", "trackbars")
    value_max = cv2.getTrackbarPos("value max", "trackbars")
    lower = np.array([h_min, sat_min, value_min]) 
    upper = np.array([h_max, sat_max, value_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    result = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow("trackbars", result)
    #29,73,165 / 57, 224, 225

    if cv2.waitKey(1 ) & 0xFF == ord('q'):
        break