import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui.catalog_page import Ui_Form
from src.CarCatalog import CarCatalog
from gui.car_description import CarDescription

import sqlite3
from sqlite3 import Error

class Catalog(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.vbox = QVBoxLayout()
        self.hBox = QHBoxLayout()
        self.carCatalog = CarCatalog()
        self.carList = self.carCatalog.getList()
        for car in self.carList:
            if car.getAvailability() != 0:
                description = CarDescription(car)
                print(car)
                self.hBox.addWidget(description)

        self.vbox.addItem(self.hBox)
        verticalSpacer = QSpacerItem(20, 80)
        self.vbox.addSpacerItem(verticalSpacer)
        self.ui.scrollAreaWidgetContents.setLayout(self.hBox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Catalog()
    w.show()
    sys.exit(app.exec_())