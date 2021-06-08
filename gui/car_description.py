import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui.link.car_description_widget import Ui_CarDescription
from src.CarCatalog import CarCatalog
from gui.checkout import Checkout
from gui.reservation import Reservation


class CarDescription(QWidget):
    def __init__(self, car):
        QWidget.__init__(self, None)
        self.ui = Ui_CarDescription()
        self.ui.setupUi(self)
        self.car = car
        self.setInfo()
        self.user = ""
        # self.checkout = Checkout()
        self.reservation = Reservation()
        self.reservation.setAttribute(Qt.WA_StyledBackground)
        self.ui.rentButton.clicked.connect(self.rentCar)

    # def rentCar(self):
    #     self.checkout.setChoosenCar(self.car)
    #     self.checkout.setAttribute(Qt.WA_StyledBackground)
    #     self.checkout.show()
    #     print(self.car)

    def rentCar(self):
        self.reservation.loadInfo(self.car, self.user)
        self.reservation.setInfo()
        self.reservation.show()

    def setUser(self, username):
        self.user = username

    def setInfo(self):
        image = QImage.fromData(self.car.getImage())
        pixmap = QPixmap().fromImage(image)
        self.ui.label.setPixmap(pixmap.scaled(380, 280, Qt.KeepAspectRatio))
        self.ui.label.setAlignment(Qt.AlignCenter)
        self.ui.brandLabel.setText(str(self.car.getBrand()))
        self.ui.modelLabel.setText(str(self.car.getCarModel()))
        self.ui.typeLabel.setText(str(self.car.getCarType()))
        self.ui.ppdLabel.setText(str(self.car.getPrice()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CarDescription(CarCatalog().getList()[0])
    w.show()
    sys.exit(app.exec_())