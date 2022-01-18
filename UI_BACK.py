

#if __name__ == '__main__':
# print('test')
from UI01 import Ui_MainWindow

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.label_3.setText("HAHAHAA")
    MainWindow.show()
    sys.exit(app.exec_())

