import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui.car_description_widget import Ui_CarDescription
from src.CarItem import CarItem
from src.CarCatalog import CarCatalog

import sqlite3
from sqlite3 import Error


class CarDescription(QWidget):
    def __init__(self, car):
        QWidget.__init__(self, None)
        self.ui = Ui_CarDescription()
        self.ui.setupUi(self)
        self.setInfo(car)

    def setInfo(self, car):
        image = QImage.fromData(car.getImage())
        pixmap = QPixmap().fromImage(image)
        self.ui.label.setPixmap(pixmap)
        self.ui.brandLabel.setText(str(car.getBrand()))
        self.ui.modelLabel.setText(str(car.getCarModel()))
        self.ui.typeLabel.setText(str(car.getCarType()))
        self.ui.pphLabel.setText(str(car.getPrice()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CarDescription(CarCatalog().getList()[0])
    w.show()
    sys.exit(app.exec_())