import cv2
import numpy as np

img = cv2.imread('resources/yaprak.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) #En uygun eşiği otomatik bulup nesneyi beyaz arka plandan ayırır


kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2) #nesne üzerindeki küçük beyaz görüntüleri temizler

sure_bg = cv2.dilate(opening, kernel, iterations=3) #nesneyi genişleterek arka planı kesin olarak belirler
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5) #Her beyaz pikselin en yakın siyah piksele olan uzaklığını hesaplar
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0) #birbirine değen nesnelerin merkezlerini tepelerini bulmamızı sağlar


sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)


ret, markers = cv2.connectedComponents(sure_fg) #her nesneye farklı bir numara verir
markers = markers + 1 #arka planı 1 yapar
markers[unknown == 255] = 0 #bilinmeyen bölgeleri 0 yapar


markers = cv2.watershed(img, markers) #sınırlar çizilir
img[markers == -1] = [0, 255, 0] # Sınırları kırmızı yap

cv2.imshow("Watershed Result", img)
cv2.waitKey(0)