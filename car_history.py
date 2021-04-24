import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from car_history_page import Ui_CarHistory

import sqlite3
from sqlite3 import Error


class CarHistory(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_CarHistory()
        self. ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CarHistory()
    w.show()
    sys.exit(app.exec_())