
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
            resim = Image.open(dosya_yolu)
            metin = pytesseract.image_to_string(resim, lang="tur")

            if metin.strip():
                self.label.setText(metin) 
                self.label.setWordWrap(True)
                self.label.setMinimumHeight(100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = UI()
    pencere.show()
    sys.exit(app.exec_())
