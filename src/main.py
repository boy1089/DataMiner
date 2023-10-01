import src.Ui as Ui
from PyQt5.QtWidgets import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure

import matplotlib
matplotlib.use('TkAgg')
from src.DataReader import DataManager
from src.StateManager.StateManager import StateManager


def main():
    app = QApplication(sys.argv)
    stateManager = StateManager()
    dataManager = DataManager()
    ex = Ui.MyApp(stateManager, dataManager)

    sys.exit(app.exec_())

    return 0



if __name__ == '__main__':
    main()

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
