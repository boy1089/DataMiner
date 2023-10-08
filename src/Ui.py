from PyQt5.QtWidgets import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from src import DataReader


class MyApp(QWidget):

    appSize = (800, 600)
    appLocation = (300, 300)
    appName = 'DataMiner'

    def __init__(self, stateManager, dataManager):
        super().__init__()
        self.initUI()
        self.stateManager = stateManager
        self.dataManager = dataManager

    def initUI(self):
        self.setWindowTitle(self.appName)
        self.move(self.appLocation[0], self.appLocation[1])
        self.resize(self.appSize[0], self.appSize[1])

        self.putButtons()

        self.canvas = FigureCanvas(Figure(figsize=(4, 3)))
        self.ax = self.canvas.figure.subplots(4, 4)


        self.vBoxLeft = QVBoxLayout()
        self.vBoxLeft.addWidget(self.btn1)
        self.vBoxLeft.addWidget(self.canvas)

        self.vBoxRight = QVBoxLayout()
        self.vBoxRight.addWidget(self.btn2)
        # self.vBoxRight.addWidget(self.canvas)

        self.hBoxRight = QHBoxLayout()
        self.hBoxRight.addWidget(self.btn3)
        self.hBoxRight.addWidget(self.btn4)

        self.vBoxRight.addLayout(self.hBoxRight)

        self.hBox = QHBoxLayout()
        self.hBox.addLayout(self.vBoxLeft, 2)
        self.hBox.addLayout(self.vBoxRight, 1)


        self.setLayout(self.hBox)

        self.show()


    def putButtons(self):

        self.btn1 = QPushButton('btn1', self)
        self.btn1.clicked.connect(self.btn1_clicked)

        self.btn2 = QPushButton('print df', self)
        self.btn2.clicked.connect(self.btn2_clicked)

        self.btn3 = QPushButton('Btn3', self)

        self.btn4 = QPushButton('Btn4', self)

    def btn1_clicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.dataManager.readData(fname[0])
        self.updateGraph()
    def btn2_clicked(self):
        print(self.dataManager.df)
    def updateGraph(self):

        for j, column in enumerate(self.dataManager.df.columns):
            ax = self.ax[j % 4][int(j / 4)]
            ax.plot(self.dataManager.df.iloc[:, self.dataManager.mainColumn], self.dataManager.df.iloc[:, j])
            ax.set_title(column)
            print(self.dataManager.df.iloc[:, j])
        # self.ax.show()
        self.canvas.draw()
        print('update done')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

