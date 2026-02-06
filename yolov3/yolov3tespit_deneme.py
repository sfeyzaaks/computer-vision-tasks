import cv2
import numpy as np

confg = "yolov3-face.cfg"
weights = "yolov3.weights"

net = cv2.dnn.readNetFromDarknet(confg, weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    if not ret:
        break
    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1/255 , (320,320), [0,0,0], swapRB= True, crop=False)
    net.setInput(blob)

    layer_names = net.getLayerNames()
    output_names =[ layer_names[i-1] for i in net.getUnconnectedOutLayers().flatten()]
    outputs = net.forward(output_names)

    boxes = []
    conf = []
    for output in outputs:
        for det in output:
            scores = det[5:]
            class_ID = np.argmax(scores)
            confidence = scores[class_ID]
            if confidence > 0.1:
                w , h = int(det[2] * w), int(det[3] * h)
                x , y = int(det[0]* w - ( w / 2)), int(det[1]*h - (h/2))

                boxes.append([x,y,w,h])
                conf.append(float(confidence))

    indices = cv2.dnn.NMSBoxes(boxes, conf, 0.1, 0.4)
    if len(indices)> 0:
        for i in indices.flatten():
            x,y,w,h = boxes[i]

            cv2.rectangle(frame, (x,y),( x+w, y+h), (0,255,0), 2 )
    cv2.imshow(frame)
            



