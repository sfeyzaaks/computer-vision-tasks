
from PIL import Image
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget, QFileDialog
import pytesseract
from PyQt5 import uic
import sys

class UI(QWidget):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("arayuz3.ui", self)
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")
        self.layouts = QVBoxLayout()

        self.button.clicked.connect(self.dosya_sec)

    def dosya_sec(self):
        dosya_yolu , _ = QFileDialog.getOpenFileName(self, "resim seç")

        if dosya_yolu:
            resim = Image.open(dosya_yolu) #seçilen dosya yolu kullanılarak resim pillow ile açılır
            metin = pytesseract.image_to_string(resim, lang="tur") #resimdeki karakterler analiz edilir ve dijital metne dönüşür

            if metin.strip():
                self.label.setText(metin) #okunan metin arayüze yansıtılır(label)
                self.label.setWordWrap(True) #eğer metin çok uzunsa alt metne geçirir
                self.label.setMinimumHeight(100) #etiketin yüksekliği ayarlanır

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = UI()
    pencere.show()
    sys.exit(app.exec_())
