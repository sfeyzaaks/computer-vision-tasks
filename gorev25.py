import open3d as o3d
import cv2
import numpy as np
from PyQt5.QtGui import QPixmap , QImage 
from PyQt5.QtWidgets import QMainWindow,  QMdiArea, QMdiSubWindow,  QPushButton, QFileDialog, QHBoxLayout,QWidget, QApplication, QLabel
from PyQt5 import uic
import torch
import sys

class UI(QMainWindow):
    count = 0

    def __init__(self):
        super(UI, self).__init__() #özellikler yüklendi
        uic.loadUi("new_win.ui", self)
        self.mdi = self.findChild(QMdiArea, "mdiArea")
        self.button = self.findChild(QPushButton, "pushButton") #designer da adı neyse o şekilde
        self.button.clicked.connect(self.add_window)
        self.show()

    def add_window(self):
        dosya_yolu , _ = QFileDialog.getOpenFileName(self, "derinleştirme için resim seçin")

        if dosya_yolu:
            UI.count += 1
            sub = QMdiSubWindow()
            pencere_icerik = QWidget()
            layout= QHBoxLayout()

            model_type = "MiDaS_small" 
            midas = torch.hub.load("intel-isl/MiDas", model_type) #indirildi
            midas.eval() #eğitim modundan çıkarıldı, sadece çıkarım için kullanılacak

            midas_transforms = torch.hub.load("intel-isl/MiDas", "transforms") 
            transform = midas_transforms.small_transform if model_type== "MiDaS_small" else midas_transforms.dpt_transform

            img = cv2.imread(dosya_yolu)
            img_rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
            input_batch = transform(img_rgb)
##########################resim işlendi
            with torch.no_grad():
                prediction = midas(input_batch) 
                prediction = torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),  
                    size = img.shape[:2], 
                    mode = "bicubic",
                    align_corners = False,
                ).squeeze()

            output = prediction.cpu().numpy()
            sub = QMdiSubWindow()
            self.lbl_derinlik = QLabel()
            output_norm = cv2.normalize(output, None, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            h, w = output_norm.shape
            q_img = QImage(output_norm.data, w, h, w, QImage.Format_Grayscale8)
            self.lbl_derinlik.setPixmap(QPixmap.fromImage(q_img).scaled(400, 300))
            sub.setWidget(self.lbl_derinlik)
            self.mdi.addSubWindow(sub)
            sub.show()

            # 3D Modeli Göster
            self.show_3d_model(output, img_rgb)
        

    def show_3d_model(self, depth_data , rgb_data):
        h, w = depth_data.shape
        x, y = np.meshgrid(np.arange(w), np.arange(h)) #her bir pikselin resim üzerindeki koordinatları belirlendi, yükseklik ve genişlik listesi oluştu
        points = np.stack((x.flatten(), y.flatten(), depth_data.flatten()), axis=1) #her bir pikselin koordinatları tek bir dizide toplandı
        colors = rgb_data.reshape(-1, 3) / 255.0 
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points) # Koordinatları yükle
        pcd.colors = o3d.utility.Vector3dVector(colors)
        pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
        o3d.visualization.draw_geometries([pcd])
       

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    pencere = UI()               
    sys.exit(app.exec_())



