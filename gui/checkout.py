import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui.checkout_ui import Ui_Form

import sqlite3
from sqlite3 import Error


class Checkout(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.car = None

        self.ui.checkoutBtn.clicked.connect(self.createOrder)

    def setChoosenCar(self, car):
        self.car = car

    def createOrder(self):
        print("Checkout")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Checkout()
    w.setAttribute(Qt.WA_StyledBackground)
    w.show()
    sys.exit(app.exec_())