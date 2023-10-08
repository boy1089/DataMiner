import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class PyQtGraphClickableExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtGraph Highlight Graph Example")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create a PlotWidget for plotting
        self.graph_widget = pg.PlotWidget(title="Clickable Graph")
        self.layout.addWidget(self.graph_widget)


        # Connect the mouseClicked signal to a callback function
        self.graph_widget.scene().sigMouseClicked.connect(self.on_graph_clicked)

        # Flag to track whether the graph is highlighted
        self.is_highlighted = False

        self.graph_widget2 = pg.PlotWidget(title="Clickable Graph")
        self.layout.addWidget(self.graph_widget2)

        # Plot some example data
        self.plot_data()

        # Connect the mouseClicked signal to a callback function
        self.graph_widget2.scene().sigMouseClicked.connect(self.on_graph_clicked2)

        # Flag to track whether the graph is highlighted
        self.is_highlighted2 = False

    def plot_data(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Plot the data with a default pen style
        self.plot = self.graph_widget.plot(x, y, pen='b', name='sin(x)')
        self.plot2 = self.graph_widget2.plot(x, y, pen='b', name='sin(x)')

    def on_graph_clicked(self, event):
        if event.button() == Qt.LeftButton:
            if not self.is_highlighted:
                # Highlight the graph by changing the pen style
                self.plot.setPen('r', width=2)  # Highlight with red color and thicker line
                self.is_highlighted = True
            else:
                # Reset the graph to its default style
                self.plot.setPen('b', width=1)  # Default blue color and line width
                self.is_highlighted = False


    def on_graph_clicked2(self, event):
        if event.button() == Qt.LeftButton:
            if not self.is_highlighted:
                # Highlight the graph by changing the pen style
                self.plot2.setPen('r', width=2)  # Highlight with red color and thicker line
                self.is_highlighted2 = True
            else:
                # Reset the graph to its default style
                self.plot2.setPen('b', width=1)  # Default blue color and line width
                self.is_highlighted2 = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PyQtGraphClickableExample()
    window.show()
    sys.exit(app.exec_())
