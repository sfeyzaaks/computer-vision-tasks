import cv2
import numpy as np
def geri_cagirma(x):
    pass
path = "resources/circles.jpg"
cv2.namedWindow("trackbars") #trackbars adında yeni bir pencere açar
cv2.resizeWindow("trackbars", 640, 540) #trackbars adındaki pencereyi boyutlandırır
cv2.createTrackbar("hue min", "trackbars", 0, 179, geri_cagirma ) #eşik değerleriyle yeni bir trackbar oluşturur
cv2.createTrackbar("hue max", "trackbars", 179, 179, geri_cagirma )
cv2.createTrackbar("sat min", "trackbars", 0, 255, geri_cagirma )
cv2.createTrackbar("sat max", "trackbars", 255, 255, geri_cagirma )
cv2.createTrackbar("value min", "trackbars", 0, 255, geri_cagirma )
cv2.createTrackbar( "value max", "trackbars", 255, 255, geri_cagirma )


while True:
    img =cv2.imread(path)
    img_resize = cv2.resize(img, (640, 480)) #resim yeniden boyutlandırıldı
    img_hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV) #hsv formatına çevirdik
    h_min = cv2.getTrackbarPos("hue min", "trackbars")#trackbarlar trackbars adındaki pencereye eklenir
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    sat_min = cv2.getTrackbarPos("sat min", "trackbars")
    sat_max = cv2.getTrackbarPos("sat max", "trackbars")
    value_min = cv2.getTrackbarPos("value min", "trackbars")
    value_max = cv2.getTrackbarPos("value max", "trackbars")
    lower = np.array([h_min, sat_min, value_min]) #min değerler dizi haline getirildi
    upper = np.array([h_max, sat_max, value_max]) #max değerler dizi haline getirildi
    mask = cv2.inRange(img_hsv, lower, upper) #min ve max değerlerle maske oluşturulur
    result = cv2.bitwise_or(img_resize,img_resize, mask= mask) #ekranda sadece seçilen renk kalır geri kalan renklerin siyah olması sağlanır
    horstack = np.hstack((img_hsv, result)) #iki farklı görüntüyü yatayda gösterir
    cv2.imshow("trackbars", horstack)
    #29,73,165 / 57, 224, 225

    if cv2.waitKey(1 ) & 0xFF == ord('q'):
        break