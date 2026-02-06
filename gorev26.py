import sys
from ultralytics import YOLO
from PyQt5.QtWidgets import QMainWindow , QPushButton , QApplication, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import uic
import cv2

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("kamera_arayuz2.ui", self)
        self.model = YOLO("yolov8n.pt")
        self.button_baslat  = self.findChild(QPushButton, "pushButton")
        self.button_durdur = self.findChild(QPushButton, "pushButton_2")
        self.label = self.findChild(QLabel, "label_camera")


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame) #timer süresi her bittiğinde update_frame fonksiyonunu çağırır
        self.button_baslat.clicked.connect(self.start_camera)
        self.button_durdur.clicked.connect(self.stop_camera)
        self.show()

    def start_camera(self): #kamerayı başlatır
        self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            self.timer.start(30) #bu komut verildiğinde qtimer saymaya başlar

    def stop_camera(self):
        self.timer.stop() 
        if hasattr(self, 'cap'): #açılmamış kamera kapatmaya çalışılırsa hata vermesini önlemek için
            self.cap.release()
        self.label.clear()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            results = self.model(frame)
            kutulanmis = results[0].plot()
            rgb_img = cv2.cvtColor(kutulanmis , cv2.COLOR_BGR2RGB) #renkleri PyQt5 in anlayacağı formata dönüştürürüz
            h, w , ch = rgb_img.shape
            bytes_per_line = ch*w #görüntünün her satırı için kaç byte olduğu hesaplanır

            convert_Qt_format = QImage(rgb_img.data , w, h , bytes_per_line, QImage.Format_RGB888 )
            p = convert_Qt_format.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation) #etiketin boyutlarına göre ayarlandı

            self.label.setPixmap(QPixmap.fromImage(p)) #etikete görüntüyü yerleştirir GPU üzerinde 

if __name__ == "__main__": #programın ana kısmı
    app = QApplication(sys.argv) #uygulama başlatıldı
    window = UI() 
    sys.exit(app.exec_()) 
    

