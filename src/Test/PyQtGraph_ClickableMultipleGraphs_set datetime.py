# additinoal layout is added
# xaxis is changed to datetim


import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
from pyqtgraph import AxisItem
import pyqtgraph as pg
class GraphWidget(pg.PlotWidget):
    def __init__(self, column_name):
        super().__init__(title=column_name, axisItems={'bottom': pg.DateAxisItem()})
        # super().__init__(title=column_name)

        # Connect the mouseClicked signal to a callback function
        self.scene().sigMouseClicked.connect(self.on_graph_clicked)

        # Flag to track whether the graph is highlighted
        self.is_highlighted = False
        self.column_name = column_name

    def update_data(self, data):
        # Update the graph with the provided data
        # x = data['a']
        x = data['datetime']
        y = data[self.column_name]
        unix_ts = [x2.timestamp() for x2 in data['datetime']]
        # Use the specified column name to select the data
        self.graph = self.plot(unix_ts, y, pen='b', name=self.column_name)  # Update the graph data

    def highlight(self):
        # Highlight the graph by changing the pen style
        self.graph.setPen(pen='r', width=2)  # Highlight with red color and thicker line
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
                if current_highlighted_graph and current_highlighted_graph != self:
                    current_highlighted_graph.unhighlight()
                current_highlighted_graph = self

current_highlighted_graph = None

class PyQtGraphGridExample(QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle("PyQtGraph Grid of Graphs Example")
        self.setGeometry(100, 100, 1000, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        # Create a grid of GraphWidgets and update with data
        self.create_graph_grid(data)

        # Create the additional layout on the right side
        self.create_additional_layout()

    def create_graph_grid(self, data):
        # Create 9 GraphWidgets and add them to the grid layout
        for i in range(3):
            for j in range(3):
                column_name = data.columns[i * 3 + j]  # Get the column name for the current graph
                graph_widget = GraphWidget(column_name)
                graph_widget.update_data(data)
                self.layout.addWidget(graph_widget, i, j)

    def create_additional_layout(self):
        # Create a container widget for the additional layout
        additional_layout_widget = QWidget()
        additional_layout_widget.setMinimumWidth(200)  # Adjust the width as needed

        # Create horizontal layout for X-axis, Y-axis, and Legend
        container_layout = QHBoxLayout()

        # Create labels for X-axis, Y-axis, and Legend titles
        x_axis_label = QLabel("X-axis")
        y_axis_label = QLabel("Y-axis")
        legend_label = QLabel("Legend")

        # Add labels to the horizontal layout
        container_layout.addWidget(x_axis_label)
        container_layout.addWidget(y_axis_label)
        container_layout.addWidget(legend_label)

        # Set the horizontal layout for the additional layout widget
        additional_layout_widget.setLayout(container_layout)

        # Add the additional layout widget to the main layout
        self.layout.addWidget(additional_layout_widget, 0, 3, 3, 1)  # Specify the row and column spans

if __name__ == '__main__':
    # Read data from the "data.py" file
    try:
        from data import df  # Assuming "data.py" contains a DataFrame named "df"
    except ImportError:
        print("Error: Make sure to create a 'data.py' file with the data as described.")
        sys.exit(1)

    app = QApplication(sys.argv)
    window = PyQtGraphGridExample(df)

    window.show()
    sys.exit(app.exec_())
