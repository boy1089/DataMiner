from PyQt5.QtWidgets import *
import sys

import pandas as pd

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('aa')
        self.move(300, 300)
        self.resize(400, 200)

        self.putButtons()
        vBox = QVBoxLayout()
        vBox.addWidget(self.btn1)


        self.setLayout(vBox)
        self.show()


    def putButtons(self):

        self.btn1 = QPushButton('btn1', self)
        self.btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        fname = QFileDialog.getOpenFileName(self)

        print(fname[0])
        print(fname[1])

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

