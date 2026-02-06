import shutil
import os

# 1. Dosyaların şu an durduğu yer (image_db4ba4.png'ye göre bir üst klasör)
kaynak = "../" 
hedef = "./" # Mevcut yolov5 klasörü

dosyalar = ["train", "valid", "test", "data.yml"]

for kalem in dosyalar:
    try:
        if os.path.exists(os.path.join(kaynak, kalem)):
            shutil.move(os.path.join(kaynak, kalem), os.path.join(hedef, kalem))
            print(f"✅ {kalem} başarıyla YOLOv5 içine taşındı.")
        else:
            print(f"❓ {kalem} bulunamadı, zaten taşınmış olabilir.")
    except Exception as e:
        print(f"❌ Hata: {e}")