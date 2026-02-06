
from PyQt5.QtWidgets import  QApplication, QMdiArea, QPushButton, QLabel,QFileDialog,QWidget
from PyQt5 import uic #tasarlanılan pencereler manuel olarak kodla yazılmadan pythona aktarıldı
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap , QImage 
from ultralytics import YOLO
import sys
import os
import cv2



class UI(QWidget): #miras alma, bir pencerenin sahip olması gereken bütün özellikler atandı
    count = 0  #açılan her bir pencereye numara vermek için

    def __init__(self):
        super(UI, self).__init__() #miras alınan sınıfa gidip oradaki özellikleri yükle
        uic.loadUi("arayuz1.ui", self)  #tasarımdaki her şey pythona yüklendi
        
        self.mdi = self.findChild(QMdiArea, "mdiArea") #çerçevemiz
        self.button = self.findChild(QPushButton, "pushButton") 
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        
        self.button.clicked.connect(self.model_sec)
        self.button2.clicked.connect(self.resim_sec)
        self.lbl_sol = self.findChild(QLabel, "label") # Qt Designer'daki adı neyse onu yaz (Genelde label'dır)
        self.lbl_sag = self.findChild(QLabel, "label_2")

        # Orijinal resmi sol tarafa tam sığdır
        
        self.show() #bilgisayar ekranında pencereyi göster

    def model_sec(self):
        # QFileDialog ile model dosyasını seçtiriyoruz
        model_yolu, _ = QFileDialog.getOpenFileName(self, "Segmentasyon Modeli Seçin" )
        
        if model_yolu:
            self.model = YOLO(model_yolu)
            self.button.setText(os.path.basename(model_yolu)) #dosya ismini buton üzerine yazar

    def resim_sec(self):  #çalışan asıl analiz motorumuz
        dosya_yolu , _ = QFileDialog.getOpenFileName(self, "Analiz için resim seçin")

        if dosya_yolu:  #eğer dosya yolu açıldıysa ve geçerli bir dosya yoluysa
            pix_orj = QPixmap(dosya_yolu)
            # scaled() fonksiyonu burada resmi büyütecek olan kısımdır
            self.lbl_sol.setPixmap(pix_orj.scaled(self.lbl_sol.width(), self.lbl_sol.height(), Qt.KeepAspectRatio))

            results = self.model.predict(dosya_yolu)
            sonuc = results[0].plot()

            rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape #yükseklik, genişlik ve renk kanalını alır
            bytes_per_line = ch*w #satır başına byte hesabı yapar
            q_img = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pix_sonuc = QPixmap.fromImage(q_img) 
            self.lbl_sag.setPixmap(pix_sonuc.scaled(self.lbl_sag.width(), self.lbl_sag.height(), Qt.KeepAspectRatio))
            
           


if __name__ == "__main__":
    app = QApplication(sys.argv) # Uygulama nesnesini oluşturur
    pencere = UI()               # Hazırladığın arayüzü başlatır
    sys.exit(app.exec_())