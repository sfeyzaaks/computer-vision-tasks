import cv2
import numpy as np

path = "resources/horse.jpg"
img_original = cv2.imread(path)
gray_img = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)
print(img_original.shape)#verilen (856,564,3) değerinde 0.karakter yüksekliği 1.karakter genişliği 2.karakter kanal sayısını verir yani renkli olduğunun göstergesidir
print(gray_img.dtype)
print(img_original.dtype)#verilen dtype uint8 tam sayı olduğunun göstergesidir
print(gray_img.size) #yükseklik*genişlik
print(img_original.size)#yükseklik*genişlik*kanal sayısı