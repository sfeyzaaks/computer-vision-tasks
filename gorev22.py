from PyQt5.QtWidgets import *
from ui2_python import Ui_MainWindow

class MainWindow(QMainWindow):
    #başlangıç fonksiyonumuz
    def __init__(self) -> None:
        super().__init__()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)
        self.qtTasarim.pushButton.clicked.connect(self.EkleTikla) #butona basılınca EkleTikla fonksiyonu çağırılır
    
    def EkleTikla(self):
        isim = self.qtTasarim.lineEdit.text() #yazılanı string formatında alır
        gsm = self.qtTasarim.lineEdit_2.text()
        print(isim, "  ", gsm)

app = QApplication([]) #yönetimi sağlar
pencere = MainWindow()
pencere.show() #hazırlanan pencere gösterilir
app.exec_()

