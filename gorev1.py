import cv2
import numpy

path = "resources/horse.jpg"
img = cv2.imread(path)
cv2.imshow("horse picture", img)
cv2.waitKey(0)
cv2.imwrite("horse.png", img)
