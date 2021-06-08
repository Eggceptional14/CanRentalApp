import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from gui.link.car_history_page import Ui_CarHistory

import sqlite3


class CarHistory(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_CarHistory()
        self. ui.setupUi(self)
        self.username = ""

    def setUser(self, user):
        self.username = user
    
    def loadData(self):
        try:

            sqliteConnection = sqlite3.connect("../db/rentalCar.db")
            cur = sqliteConnection.cursor()
            cur.execute("SELECT carId, carModel, interval, pickupTime, returnTime, branch FROM userHistory WHERE userName=?", (self.username,))
            rows = cur.fetchall()

            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(rows):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CarHistory()
    w.setUser("Smith")
    w.loadData()
    w.show()
    sys.exit(app.exec_())