import cv2
import numpy as np
path = "resources/shapes.png"
img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray_img, 50, 0.01, 15, useHarrisDetector=True, k=0.1) #köşe tespiti için kıullanılan fonksiyon
corner = np.int32(corners) #resim 32 bitlik tam sayı değerine getirildi
for c in corner:
    x,y = c.ravel() #birden fazla boyutlu olan diziyi tek bri diziye indirgedi
    img = cv2.circle(img,(x,y),5,(0,0,255),-1) #verilen koordinatlara kırmızı daire çiz
cv2.imshow("corner detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


###edge
import cv2

path = "resources/shapes.png"
img = cv2.imread(path)
blurred = cv2.GaussianBlur(img, (5,5),0) #resim blurlandı
edged = cv2.Canny(blurred,100,200)
cv2.imshow("edged",edged)
cv2.waitKey(0)