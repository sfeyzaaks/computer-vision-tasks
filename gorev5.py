import cv2
import numpy as np

path = "resources/horse.jpg"
img = cv2.imread(path)
img_1 = np.uint8(img)
cv2.rectangle(img_1 , (0,0), (564,846), (0,255,255),10)
img_gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,15)#blurlamanın şiddeti
                            , 0) #blurlama işlemi gerçekleştirildi
cv2.imshow("the gray one", img_gray)
cv2.imshow("the gray one with blur", img_blur)
cv2.waitKey(0)
#her pikselin üç ayrı parlaklık değeri vardır. Birçok bilgisayarlı görü algoritması daha çok renk parlaklıklarıyla ilgilendiği için gri tonlama yapma, iş yükünü 
#azaltır ve performansı arttırır. Bunun örneğini tıbbi görüntülemelerde görebiliriz. x ışını ve ultrason gibi görüntüler griye çevrilerek tanı daha kolay konulur.
#Blurlama ise sensör hatalarından kaynaklanan keskin görüntüleri yumuşatmaya yarar.Canny ise görüntüdeki sadece önemli ve keskin detaylara odaklanmamızı sağlar.
#Aynı zamanda blurlama işlemi ile günlük hayatta tanınmayan kişilerin blurlanması sağlanabilir.
#Kısacası gri tonlama ile görüntüler sadeleştirir blurlama ile ise gürültü azaltılmış olur.