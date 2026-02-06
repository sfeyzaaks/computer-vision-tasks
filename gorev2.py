import cv2

path = "resources/horse.jpg"
img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #resim bu fonksiyonla gri renge dönüştürülür
cv2.imshow("gray picture", img_gray) #griye dönüştürülmüş resim
cv2.imshow("horse", img) #orijinal resim
cv2.waitKey(0)