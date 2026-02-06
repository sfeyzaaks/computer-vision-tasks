import cv2

path = "resources/yaprak.jpg"
img = cv2.imread(path)
cv2.imshow("yaprak resmi", img)
img_thresholding = cv2.threshold(img, 127 #min eşik değeri
                                 , 255 #max eşik değeri
                                 , cv2.THRESH_BINARY)[1] #iki değer alırız, biz sadece işlenmiş görüntüyü almak istiyoruz

cv2.imshow("yaprak thresholding", img_thresholding)
cv2.waitKey(0)

#thresholding : her pikselin kenar kalınlığını belirlenmiş bir eşik değerle karşılaştırma işlemidir. mesela her pikselin kenar kalınlığı 
# (100,200) değerindeki alt eşik ve üst eşikle karşılaştırılabilir.
# temel amaç gürültüyü azaltmak ve nesneleri arka plandan keskin bir şekilde ayırmaktır.
#günlük hayatta somut olan belgeleri( el yazısı vs.) dijital ortama aktarılmasını sağlar.
# kalite kontrolünde belirlenmiş eşiğin üzerindeki nesnelerin ve anormalliklerin ortaya çıkmasını sağlar.
#özellikle tıbbi görüntülemede tümör doku zedelenmesinin vs. fark edilmesini sağlar.
# parmak izinin taranmasının ardından izlerin belirgin olması sağlanabilir.
# kısacası önemli görülen kısımların belirginleşmesini sağlayarak bir sonraki adıma karmaşıklaşmadan geçilmesini sağlar.
