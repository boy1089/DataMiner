import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt5.QtCore import Qt

current_highlighted_graph = None

class GraphWidget(pg.PlotWidget):

    def __init__(self, title):
        super().__init__(title=title)

        # Plot some example data
        self.plot_data()

        # Connect the mouseClicked signal to a callback function
        self.scene().sigMouseClicked.connect(self.on_graph_clicked)

        # Flag to track whether the graph is highlighted
        self.is_highlighted = False

    def plot_data(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Plot the data with a default pen style
        self.graph = self.plot(x, y, pen='b', name='sin(x)')

    def highlight(self):
        # Highlight the graph by changing the pen style
        self.graph.setPen(pen='w', width=3)  # Highlight with red color and thicker line

        self.is_highlighted = True

    def unhighlight(self):
        # Reset the graph to its default style
        self.graph.setPen(pen='b', width=1)  # Default blue color and line width
        self.is_highlighted = False

    def on_graph_clicked(self, event):
        global current_highlighted_graph

        if event.button() == Qt.LeftButton:
            if not self.is_highlighted:

                # Highlight the clicked graph
                self.highlight()
                # Unhighlight the previously highlighted graph (if any)
                if (current_highlighted_graph != None ) and (current_highlighted_graph != self):
                    current_highlighted_graph.unhighlight()
                current_highlighted_graph = self

class PyQtGraphGridExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtGraph Grid of Graphs Example")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        # Create a grid of GraphWidgets
        self.create_graph_grid()

    def create_graph_grid(self):
        # Create 9 GraphWidgets and add them to the grid layout
        for i in range(3):
            for j in range(3):
                graph_widget = GraphWidget(title=f"Graph {i * 3 + j + 1}")
                self.layout.addWidget(graph_widget, i, j)

if __name__ == '__main__':
    current_highlighted_graph = None

    app = QApplication(sys.argv)
    window = PyQtGraphGridExample()
    window.show()
    sys.exit(app.exec_())
