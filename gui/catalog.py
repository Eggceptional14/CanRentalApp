import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from catalog_page import Ui_Form

import sqlite3
from sqlite3 import Error

class Catalog(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Catalog()
    w.show()
    sys.exit(app.exec_())