import cv2
import numpy as np

path = "resources/horse.jpg"
img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray picture", img_gray)
cv2.imshow("horse", img)
cv2.waitKey(0)