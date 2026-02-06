import cv2
import numpy as np


weights_path = 'yolov3.weights'
config_path = 'yolov3-face.cfg'


net = cv2.dnn.readNetFromDarknet(config_path, weights_path) #opencv ile yolov3 modelini yükler
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #kamera okunur frame alınır
    if not ret:
        break

    H, W = frame.shape[:2] #görüntünün yükseklik ve genişliği alınır

    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), [0, 0, 0], swapRB=True, crop=False) #ham görüntü derin öğrenme modelinin giriş katmanına uygun hale getirilir
    net.setInput(blob) #hazırlanan görüntü modele verilir
    

    layer_names = net.getLayerNames() #tüm katmanların ismi bir liste olarak alınır
    output_names = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()] #sadece sayılardan oluşan basit bir diziye dönüştürüldü
    outputs = net.forward(output_names) #tespit edilen nesnein koordinatları ve güven aralıkları
    
    #modelden gelen tahminleri saklamak için boş listeler oluşturuldu
    boxes = []
    confidences = []

    for output in outputs: #her bir görüntüdeki
        for det in output: #her bir yüz
            scores = det[5:] #nesnelerin kimliği alınır
            classId = np.argmax(scores) #en yüksek skora sahip olan alınır
            confidence = scores[classId] #en yüksek güven aralığını alıp kaydeder
      
            if confidence > 0.2:
                w, h = int(det[2] * W), int(det[3] * H) #modelden gelen genişlik ve yükseklik oranları
                x, y = int((det[0] * W) - w / 2), int((det[1] * H) - h / 2) #merkezden genişliğin yarısı çıkarılarak sol üst köşe bulunur
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))

  
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4) 
    

    if len(indices) > 0:
        for i in indices.flatten(): #veriler düzleştirilir
            x, y, w, h = boxes[i] #sol üst köşe koordinatları ve boyutları geri çağırıldı
         
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #belirlenen nesneye dörtgen çizildi
          
            label = f'Yuz: %{int(confidences[i]*100)}' #yüzde yazılır
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


    cv2.imshow('YOLOv3 Yüz Tespiti', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()