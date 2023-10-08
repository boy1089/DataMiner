import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QBrush
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotWidget(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.figure = Figure(figsize=(width / 80, height / 80), dpi=80)
        self.canvas = FigureCanvas(self.figure)

        self.plot_data()

    def plot_data(self):
        ax = self.figure.add_subplot(111)
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)
        ax.plot(x, y)
        self.canvas.draw()

        # Create an image from the canvas
        img = self.canvas.buffer_rgba()

        # Convert the image to a QImage
        qimg = QImage.fromData(img)

        # Create a QPixmap from the QImage
        pixmap = QPixmap.fromImage(qimg)

        # Create a QBrush from the QPixmap
        brush = QBrush(pixmap)

        # Set the brush of the QGraphicsRectItem
        self.setBrush(brush)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Embedded Graph in QGraphicsRectItem")
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        # Create and add a QGraphicsRectItem containing the plot
        plot_item = PlotWidget(100, 100, 400, 300)
        self.scene.addItem(plot_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
