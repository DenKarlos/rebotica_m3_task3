from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QSlider, QWidget
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Gallery(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Галерея изображений")
        self.resize(800, 600)

        self.imgs = [
            ('imgs/nature01.jpg', 'горное озеро'), 
            ('imgs/nature02.jpg', 'дорога в горах'), 
            ('imgs/nature03.jpg', 'альпийский луг'), 
            ('imgs/nature04.jpg', 'озеро у одинокой горы'), 
            ('imgs/nature05.jpg', 'вид на море с утёса'), 
            ('imgs/nature06.jpg', 'озеро утром'), 
            ('imgs/nature07.jpg', 'озеро в тумане'), 
            ('imgs/nature08.jpg', 'скалистый берег'), 
            ('imgs/nature09.jpg', 'пирс у озера утром'), 
            ('imgs/nature10.jpg', 'поезд в Альпах')
        ]

        self.img_lbl = QLabel()
        self.img_lbl.setAlignment(Qt.AlignCenter)
        
        self.discr_lbl = QLabel()
        self.discr_lbl.setAlignment(Qt.AlignCenter)
                
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, len(self.imgs) - 1)
        self.slider.setValue(0)
        
        self.slider.valueChanged.connect(self.change_img)

        layout = QVBoxLayout()
        layout.addWidget(self.img_lbl)
        layout.addWidget(self.discr_lbl)
        layout.addWidget(self.slider)
        
        self.setLayout(layout)        
        self.change_img(0)

    def change_img(self, index):
        pixmap = QPixmap(self.imgs[index][0])
        pixmap = pixmap.scaled(
            550, 400,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.img_lbl.setPixmap(pixmap)
        
        discr = self.imgs[index][1]
        self.discr_lbl.setText(f"Изображение {index + 1} из {len(self.imgs)}\n{discr}")

def application():
    app = QApplication(sys.argv)
    window = Gallery()
    window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    application()