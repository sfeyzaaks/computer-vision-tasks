import cv2
import numpy as np

path = "resources/horse.jpg"
img = cv2.imread(path)
img_1 = np.uint8(img)
cv2.rectangle(img_1 , (0,0), (564,846), (0,255,255),10)

cv2.imshow("square", img_1)
cv2.waitKey(0)