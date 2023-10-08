import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QMainWindow
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MatplotlibGraphItem(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.figure = Figure(figsize=(width / 80, height / 80), dpi=80)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(None)

        self.setFlag(QGraphicsRectItem.ItemHasNoContents, False)

        self.plot_graph()

    def plot_graph(self):
        ax = self.figure.add_subplot(111)
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)
        ax.plot(x, y)
        self.canvas.draw()

    def paint(self, painter, option, widget):
        pixmap = self.canvas.get_cached_background()
        if pixmap.isNull():
            self.canvas.draw()
            pixmap = self.canvas.get_cached_background()
        painter.drawPixmap(int(self.x()), int(self.y()), pixmap)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib Graph in QGraphicsRectItem")
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        # Create and add a QGraphicsRectItem containing the Matplotlib graph
        graph_item = MatplotlibGraphItem(100, 100, 400, 300)
        self.scene.addItem(graph_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
