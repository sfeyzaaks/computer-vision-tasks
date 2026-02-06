import cv2
import numpy as np
path = "resources/horse.jpg"
img = cv2.imread(path)
img_canny = cv2.Canny(img,100,200) #kenarlar belirginleştirilir
kernel = np.ones((5,5),np.uint8)
img_dilate = cv2.dilate(img_canny,kernel,iterations = 1) #canny ile bulunan kenarlar kalınlaştılır
img_erosion = cv2.erode(img_dilate,kernel,iterations =1) #kalınlaşan kenarları tekrar inceltir
kapali_img = cv2.morphologyEx(img_erosion , cv2.MORPH_CLOSE , kernel) #önce dilation daha sonra erodiation işlemi yapar
cv2.imshow("img",kapali_img)
cv2.waitKey(0)