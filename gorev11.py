import cv2

path = "resources/horse.jpg"
img =cv2.imread(path)
img_reverse = cv2.flip(img,0)#alta döndürür
img_reverse_1 = cv2.flip(img,1) #sağa döndürür
img_reverse_2 =cv2.flip(img,-1) #sağa ve alta çevirir
cv2.imshow("flip metodu",img_reverse)
cv2.waitKey(0)

