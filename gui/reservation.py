import sys

from PySide6.QtWidgets import *
import sqlite3
from sqlite3 import Error
from datetime import date
from gui.link.reservation_page import Ui_MainWindow

class Reservation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.car = None
        self.user = ""
        self.dbConnection = None
        self.initDBConnection()

        #list of information
        self.info = []

        #combo box setup
        branches = ["rama 3", "Sathorn", "Ladkrabang", "Rangsit", "Siam"]
        for b in branches:
                self.ui.serviceBranch_comboBox.addItem(b)

        #model list setup
        self.ui.setInfo_button.clicked.connect(self.display)
        self.ui.confirm_button.clicked.connect(self.confirm)

    def initDBConnection(self):
        try:
            self.dbConnection = sqlite3.connect("../db/rentalCar.db")
            print("connected to database")
        except Error as e:
            print(e)

    def loadInfo(self, car, user):
        self.car = car
        self. user = user
        self.setInfo()

    def setInfo(self):
        self.ui.modelLabel.setText(self.car.getCarModel())
        self.ui.priceLabel.setText(str(self.car.getPrice()) + " ฿")

    def display(self):

        ppd = self.car.getPrice()

        #interval
        startD = int(self.ui.pickup_dateEdit.date().day())
        startM = int(self.ui.pickup_dateEdit.date().month())
        startY = int(self.ui.pickup_dateEdit.date().year())
        start = str(startD) + "/" + str(startM) + "/" + str(startY)

        endD = int(self.ui.return_dateEdit.date().day())
        endM = int(self.ui.return_dateEdit.date().month())
        endY = int(self.ui.return_dateEdit.date().year())
        end = str(endD) + "/" + str(endM) + "/" + str(endY)

        interval = str(start) + " to " + str(end)
        self.ui.intervalLabel.setText(interval)
        
        #no. of days
        s_date = date(startY, startM, startD)
        e_date = date(endY, endM, endD)
        delta = e_date - s_date
        days = delta.days

        #return same date
        if days == 0:
            days = 1
        self.ui.totalDayLabel.setText(str(days))

        #service branch
        branch = self.ui.serviceBranch_comboBox.currentText()
        self.ui.branchLabel.setText(branch)

        #price
        price = ppd * days
        self.ui.totalPriceLabel.setText(str(price) + " baht")

        #time
        pickup_time = self.ui.pickup_timeEdit.time().toString()
        return_time = self.ui.return_timeEdit.time().toString()

        #gather all information(username, carmodel, interval, pick-up time, return time, branch, total income)
        self.info = [self.user, self.car.getCarId(), self.car.getCarModel(), interval, pickup_time, return_time, branch, price]
        
    def confirm(self):
        #update car avilability
        result = self.dbConnection.cursor().execute("""UPDATE carInformation SET available = 0 WHERE car_id = ?""",(self.car.getCarId(),))
        self.dbConnection.commit()
        # item = self.ui.listWidget.currentItem()
        # self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

        #insert data into the database
        adminTable = self.dbConnection.cursor().execute("""INSERT INTO admin(username, carId, carModel, interval, pickupTime, returnTime, branch, income)VALUES(?,?,?,?,?,?,?,?)""", tuple(self.info))
        self.dbConnection.commit()

        #insert data to userHistory
        adminTable = self.dbConnection.cursor().execute("""INSERT INTO userHistory(username, carId, carModel, interval, pickupTime, returnTime, branch, price)VALUES(?,?,?,?,?,?,?,?)""", tuple(self.info))
        self.dbConnection.commit()


        dialog = QMessageBox()
        dialog.setText("Reservation successful")
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Reservation()
    w.show()
    sys.exit(app.exec_())