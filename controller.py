from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap


import cv2

from UI01 import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
#        self.setup_control()
#        self.horizontalSlider_valueChanged()
#        self.load_image()
        self.photo_resize()

    def setup_control(self):
        # TODO
        self.ui.label.setText('Happy World!')
        self.clicked_counter = 0
        self.ui.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        # self.clicked_counter += 1
        # print(f"You clicked {self.clicked_counter} times.")

        msg = self.ui.lineEdit.text()
        self.ui.label.setText(msg)
#拉霸

    def horizontalSlider_valueChanged(self):
        self.ui.horizontalSlider.valueChanged.connect(self.getslidervalue)

    def getslidervalue(self):
        self.ui.label_3.setText(f"{self.ui.horizontalSlider.value()}")
        #print(self.ui.horizontalSlider.value())

#讀入圖片1

    def load_image(self):
        # TODO
        self.img_path = 'car.jpeg'
        self.display_img()

#讀入圖片Show圖主程式

    def display_img(self):
        self.img = cv2.imread(self.img_path)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))

#改變圖片大小
    def photo_resize(self):
        # TODO
        self.img_path = 'car2.jpeg'
        self.ui.btn_zoom_in.clicked.connect(self.func_zoom_in)
        self.ui.btn_zoom_out.clicked.connect(self.func_zoom_out)
        self.display_img2()

#改變圖片大小 主程式
    def display_img2(self):
        self.img = cv2.imread(self.img_path)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))

#Zoom in
    def func_zoom_in(self):
        self.qpixmap_height -= 100
        self.resize_image()

# Zoom OUT
    def func_zoom_out(self):
        self.qpixmap_height += 100
        self.resize_image()

# Zoomin zoonout Show 圖功能
    def resize_image(self):
        scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        self.ui.label.setPixmap(scaled_pixmap)




