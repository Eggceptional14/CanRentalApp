import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui.profile_ui import Ui_Form
from gui.car_history import CarHistory

import sqlite3
from sqlite3 import Error


class Profile(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.rentHsBtn.clicked.connect(self.showHistory)
        self.history = CarHistory()

    def loadData(self):
        pass

    def showHistory(self):
        self.history.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Profile()
    w.setAttribute(Qt.WA_StyledBackground)
    w.show()
    sys.exit(app.exec_())