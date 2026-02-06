from PyQt5.QtWidgets import *
from ui2_python import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)
        self.qtTasarim.pushButton.clicked.connect(self.EkleTikla)

    def EkleTikla(self):
        isim = self.qtTasarim.lineEdit.text()
        gsm = self.qtTasarim.lineEdit_2.text()
        print(isim, "  ", gsm)

app = QApplication([])
pencere = MainWindow()
pencere.show()
app.exec_()

