import cv2

path = "resources/horse.jpg"
img = cv2.imread(path)
cv2.imshow("the original one", img)
print(img.shape) 
img_resized = cv2.resize(img, (650,440)) #görselin boyutları(yükseklik, genişlik, kanal sayısı) gösterilir
img_cropped = img_resized[0:220,0:300] #görseli yeniden boyutlandırır
cv2.imshow("the resized one", img_resized)
cv2.imshow("the horse head", img_cropped)
cv2.waitKey(0)
cv2.waitKey(0)

#######alternative

path = "resources/horse.jpg"
img = cv2.imread(path)
cv2.imshow("the original one", img)
print(img.shape)
img_resized = cv2.resize(img, (650,440))
img_cropped = img_resized[0:220,0:300] #resim kırpılır
img_cropppedone = cv2.resize(img_cropped , (img.shape[1], img.shape[0])) #kırpılan orijinal resmin boyutlarına geri döndürülür
cv2.imshow("cropped", img_cropppedone)
cv2.imshow("the resized one", img_resized)
cv2.imshow("the horse head", img_cropped)
cv2.waitKey(0)
cv2.waitKey(0)