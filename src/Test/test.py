

class Graph(pg.PlotWidget):

    def __init__(self):
        super().__init__()

        self.scene().sigMouseClicked.connect(self.onClicked)
        self.is_highlighted = False

    def plotGraph(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Plot the data with a default pen style
        self.plot = self.plot(x, y, pen='b', name='sin(x)')

    def onClicked(self, event):

        return 0


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
        self.graph_widget = Graph()
        self.layout.addWidget(self.graph_widget)

        # Connect the mouseClicked signal to a callback function
        self.graph_widget.scene().sigMouseClicked.connect(self.on_graph_clicked)

        # Flag to track whether the graph is highlighted
        self.is_highlighted = False

        self.graph_widget2 = Graph()
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
        if