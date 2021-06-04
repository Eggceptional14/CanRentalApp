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

        self.hBox = QHBoxLayout()
        self.carCatalog = CarCatalog()

        self.carList = self.createCarList(self.carCatalog.getList())
        self.addCatalogItem(self.carList)

        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setLayout(self.hBox)
        self.ui.scrollArea.setWidget(self.scrollAreaWidget)

        self.ui.checkoutBtn.clicked.connect(self.checkout)
        self.ui.profileBtn.clicked.connect(self.profile)
        self.ui.setFilterBtn.clicked.connect(self.setFilter)

        self.brandFilter = ""
        self.typeFilter = ""
        self.priceRange = []

        self.rentedCarList = []

        self.ui.brandComboBox.addItem("Any")
        self.ui.typeComboBox.addItem("Any")
        self.ui.brandComboBox.addItems(self.carCatalog.getBrandList())
        self.ui.typeComboBox.addItems(self.carCatalog.getCarTypeList())

    def createCarList(self, items):
        carList = []
        for item in items:
            carList.append(item)
        return carList

    def addCatalogItem(self, items):
        for car in items:
            description = CarDescription(car)
            # print(car)
            description.ui.rentButton.clicked.connect(self.rent)
            self.hBox.addWidget(description)

    def rent(self):
        sender = self.sender()
        print(sender.text())

    def profile(self):
        print("profile")

    def updateCatalogItem(self):
        carList = set()
        brand = self.carCatalog.brandFilter(self.brandFilter)
        carType = self.carCatalog.typeFilter(self.typeFilter)
        priceRange = self.carCatalog.setPriceRange(self.priceRange)
        carList = set(brand) & set(carType) & set(priceRange)

        if len(carList) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.info)
            msg.setText("No Available Car")
            msg.setInformativeText("")
            msg.setWindowTitle("No Available Car")
            msg.exec_()
        else:
            self.clearItems()
            self.carList = carList
            self.addCatalogItem(self.carList)
            self.scrollAreaWidget.setLayout(self.hBox)
    
    def clearItems(self):
        for i in reversed(range(self.hBox.count())):
            self.hBox.itemAt(i).widget().setParent(None)

    def checkout(self):
        pass

    def setFilter(self):

        if self.ui.priceFrom.text().isdigit() and self.ui.priceTo.text().isdigit():
            
            if int(self.ui.priceFrom.text()) > int(self.ui.priceTo.text()):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error: Invalid price range entry.")
                msg.setInformativeText("")
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                self.priceRange.append(int(self.ui.priceFrom.text()))
                self.priceRange.append(int(self.ui.priceTo.text()))
            # print(self.ui.priceFrom.text())
            # print(self.ui.priceTo.text())
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error: Price range carFilter only allowed integers.")
            msg.setInformativeText("")
            msg.setWindowTitle("Error")
            msg.exec_()

        self.brandFilter = self.ui.brandComboBox.currentText()
        self.typeFilter = self.ui.typeComboBox.currentText()

        # print(self.brandFilter)
        # print(self.typeFilter)
        self.updateCatalogItem()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Catalog()
    w.setAttribute(Qt.WA_StyledBackground)
    w.setWindowTitle("CarRentalApp")
    w.show()
    sys.exit(app.exec_())