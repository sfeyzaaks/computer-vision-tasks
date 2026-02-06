import cv2

path = "resources/horse.jpg" #resim yolu
img = cv2.imread(path) #resim okunur
cv2.imshow("horse picture", img) #resim gösterilir
cv2.waitKey(0) #resmin ne kadar ekranda kalacağını gösteren fonksiyon
cv2.imwrite("horse.png", img) #dosyayı kaydeder
