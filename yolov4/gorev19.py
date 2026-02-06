import cv2
import time

#dosya yolları
config_path = "yolov4-tiny.cfg"
weight_path = "yolov4-tiny.weights"
names_path = "coco.names"

with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]


net = cv2.dnn.readNetFromDarknet(config_path, weight_path) #model yüklendi
model = cv2.dnn_DetectionModel(net)

model.setInputSize(416, 416) #görüntü boyutu
model.setInputScale(1.0 / 255.0) #normalizasyon yapılarak işlemler hızlandırıldı
model.setInputSwapRB(True) #modelin renkleri doğru algılaması için renk kanallarının yeri değiştirildi
cap = cv2.VideoCapture(0)

pTime = 0

while True:
    ret , frame = cap.read() #video görüntüsü okundu
    if not ret:
        break
    
    class_ids , scores , boxes = model.detect(frame, confThreshold = 0.3 , nmsThreshold = 0.4) #görüntü üzerinden güven aralıkları belirlendi

    for (class_id, score , box) in zip(class_ids , scores, boxes ):
        if classes == "person":
            cv2.rectangle(frame,box, (0,255,0),2) #her bir insan görüntüsüne kare çizer

    cTime = time.time() #şu anki zaman kaydedilir
    fps = 1 / (cTime - pTime) #fps hesaplanır
    pTime = cTime #şu anki zamanı bir sonraki kare için "eski zaman" olarak kaydet

    cv2.putText(frame, f"{int(fps)}", (frame.shape[1]-120 , 50),cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2) #frame köşesine fps yazılır

    cv2.imshow("yolov4",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break
