import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import Qt

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

    def on_graph_clicked(self, event):
        if event.button() == Qt.LeftButton:
            if not self.is_highlighted:
                # Highlight the graph by changing the pen style
                self.plotItem.plot(pen='r', width=2)  # Highlight with red color and thicker line
                self.graph.setPen('r', width=2)  # Highlight with red color and thicker line
                self.is_highlighted = True
            else:
                # Reset the graph to its default style
                self.plotItem.plot(pen='b', width=1)  # Default blue color and line width
                self.graph.setPen('b', width=2)  # Highlight with red color and thicker line
                self.is_highlighted = False

