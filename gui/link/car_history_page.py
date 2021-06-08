# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'car_history_page.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_CarHistory(object):
    def setupUi(self, CarHistory):
        if not CarHistory.objectName():
            CarHistory.setObjectName(u"CarHistory")
        CarHistory.resize(699, 501)
        CarHistory.setStyleSheet(u"background-color:white;")
        self.tableWidget = QTableWidget(CarHistory)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 110, 611, 351))
        self.tableWidget.setStyleSheet(u"background: none;background-color: white;border-radius: 10px;border-style: outset;border-width: 2px;border-color: #0c7b93; QHeaderView::section {background-color: white;padding: 4px;border: 0px;font-size: 14pt;}"
"\n"
"\n"
"\n"
"")
        self.frame = QFrame(CarHistory)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 661, 421))
        self.frame.setStyleSheet(u"background-color:white; border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 131, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #0d7377;background-color: white;")
        self.frame.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(CarHistory)

        QMetaObject.connectSlotsByName(CarHistory)
    # setupUi

    def retranslateUi(self, CarHistory):
        CarHistory.setWindowTitle(QCoreApplication.translate("CarHistory", u"History", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CarHistory", u"Car Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CarHistory", u"Car Model", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CarHistory", u"Interval", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CarHistory", u"Pickup time", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CarHistory", u"Return time", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CarHistory", u"Branch", None));
        self.label.setText(QCoreApplication.translate("CarHistory", u"Car History", None))
    # retranslateUi

