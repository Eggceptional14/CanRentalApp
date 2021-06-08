import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from gui.link.checkout_ui import Ui_Form

import sqlite3
from sqlite3 import Error


class Checkout(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.car = None
        self.username = ""

        self.ui.checkoutBtn.clicked.connect(self.createOrder)
        # self.recordCarReservation(car, self.getUsername())

    def setChoosenCar(self, car):
        self.car = car
        self.ui.brandLabel.setText(self.car.getBrand())
        self.ui.typeLabel.setText(self.car.getCarType())
        self.ui.modelLabel.setText(self.car.getCarModel())
        self.ui.priceLabel.setText(str(self.car.getPrice()) + " Baht")

    def createOrder(self):
        # print(self.username)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        message = "Reservation ID: {resvId}\n\
                    From {sDate} to {rDate}\n\
                    Car ID: {cId} {cBrand} {cModel}".format(resvId=self.getReservationId(), sDate=self.getStartDate(), rDate=self.getReturnDate(),
                                                            cId=self.car.getCarId(), cBrand=self.car.getBrand(), cModel=self.car.getCarModel())

        msg.setText("Checkout:")
        msg.setWindowTitle("Checkout")
        msg.setDetailedText(message)
        msg.setStandardButtons(QMessageBox.Ok)

        self.recordCarReservation(self.car, self.username)
        msg.exec_()

    def setUsername(self, username):
        self.username = username
    
    def getUsername(self):
        return self.username

    def getStartDate(self):
        return self.ui.startInput.text()

    def getReturnDate(self):
        return self.ui.endInput.text()

    def getReservationId(self):
        conn = None
        try:
            conn = sqlite3.connect("../db/rentalCar.db")
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT (*) FROM reservationHistory")
            rowcount = cursor.fetchone()[0]
            return rowcount
        except Error as e:
            print(e)

    def recordCarReservation(self, car, userName):
        reservationId = self.getReservationId()
        carId = car.getCarId()
        startDate = self.getStartDate()
        endDate = self.getReturnDate()

        try:
            sqliteConnection = sqlite3.connect("../db/rentalCar.db")
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO reservationHistory
                            (reservationId, carId, userName, startDate, endDate) 
                            VALUES (?, ?, ?, ?, ?);"""

            data_tuple = (reservationId, carId, userName, startDate, endDate)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Inserted successfully")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Checkout()
    w.setAttribute(Qt.WA_StyledBackground)
    w.show()
    sys.exit(app.exec_())