import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui.car_description_widget import Ui_CarDescription
from src.CarCatalog import CarCatalog
from gui.checkout import Checkout

import sqlite3
from sqlite3 import Error


class CarDescription(QWidget):
    def __init__(self, car):
        QWidget.__init__(self, None)
        self.ui = Ui_CarDescription()
        self.ui.setupUi(self)
        self.car = car
        self.setInfo()
        self.history = Checkout()
        self.ui.rentButton.clicked.connect(self.rentCar)

    def rentCar(self):
        self.history.setChoosenCar(self.car)
        self.history.setAttribute(Qt.WA_StyledBackground)
        self.history.show()
        print(self.car)

    def setInfo(self):
        image = QImage.fromData(self.car.getImage())
        pixmap = QPixmap().fromImage(image)
        self.ui.label.setPixmap(pixmap.scaled(380, 280, Qt.KeepAspectRatio))
        self.ui.label.setAlignment(Qt.AlignCenter)
        self.ui.brandLabel.setText(str(self.car.getBrand()))
        self.ui.modelLabel.setText(str(self.car.getCarModel()))
        self.ui.typeLabel.setText(str(self.car.getCarType()))
        self.ui.pphLabel.setText(str(self.car.getPrice()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CarDescription(CarCatalog().getList()[0])
    w.show()
    sys.exit(app.exec_())