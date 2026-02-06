import cv2

config_path = "yolov4-tiny.cfg"
weight_path = "yolov4-tiny.weights"
names_file = "coco.names"
img_path = "images.jpeg"


with open(names_file , "r") as f:
    classes = [line.strip() for line in f.readlines()]

net = cv2.dnn.readNetFromDarknet(weight_path, config_path)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size = (416,416), scale = 1/255, swapRB = True)

img = cv2.imread(img_path)

class_ids, scores, boxes = model.detect(img, confThreshold= 0.5, nmsThreshold = 0.4)

person_count = 0
for (class_id, score, box) in zip(class_ids, scores, boxes):
    if classes[class_ids] == "person":
        person_count += 1
        x, y, w, h = box

        cv2.rectangle(img , (x, y-10),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), 2 )
cv2.imshow(img)
