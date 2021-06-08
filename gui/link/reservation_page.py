# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservation.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import assets.images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 450)
        MainWindow.setMinimumSize(QSize(650, 450))
        MainWindow.setMaximumSize(QSize(650, 450))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-image: url(:/login/login_background.png);\n"
"}\n"
"\n"
"QFrame {\n"
"	background: #d9d9d9;\n"
"	border: 1px solid #d9d9d9;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"\n"
"QDateEdit {\n"
"	background: white;\n"
"}\n"
"\n"
"QTimeEdit {\n"
"	background: white;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background: white;\n"
"}"
 "\n""QComboBox QAbstractItemView{\n"
 "	color: black;\n"
 "   font: 16px;"
 "	background: none;\n"
 "	background-color: white;\n"
 "	border-radius: 10px;\n"
 "   padding-left: 4px;\n"
 "}\n"
 "\n"
"QComboBox QAbstractItemView::item:hover{\n"
 "	background: none;\n"
 "   color: grey;\n"
 "}\n"
 "\n"

 )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"	font-weight: bold;\n"
"	color:white;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background: none;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pickup_label = QLabel(self.frame)
        self.pickup_label.setObjectName(u"pickup_label")

        self.verticalLayout.addWidget(self.pickup_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pickup_dateEdit = QDateEdit(self.frame)
        self.pickup_dateEdit.setObjectName(u"pickup_dateEdit")
        self.pickup_dateEdit.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pickup_dateEdit)

        self.pickup_timeEdit = QTimeEdit(self.frame)
        self.pickup_timeEdit.setObjectName(u"pickup_timeEdit")

        self.horizontalLayout.addWidget(self.pickup_timeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.return_dateEdit = QDateEdit(self.frame)
        self.return_dateEdit.setObjectName(u"return_dateEdit")

        self.horizontalLayout_2.addWidget(self.return_dateEdit)

        self.return_timeEdit = QTimeEdit(self.frame)
        self.return_timeEdit.setObjectName(u"return_timeEdit")

        self.horizontalLayout_2.addWidget(self.return_timeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.selectBranch_label = QLabel(self.frame)
        self.selectBranch_label.setObjectName(u"selectBranch_label")

        self.verticalLayout.addWidget(self.selectBranch_label)

        self.serviceBranch_comboBox = QComboBox(self.frame)
        self.serviceBranch_comboBox.setObjectName(u"serviceBranch_comboBox")
        self.serviceBranch_comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}")

        self.verticalLayout.addWidget(self.serviceBranch_comboBox)

        self.setInfo_button = QPushButton(self.frame)
        self.setInfo_button.setObjectName(u"setInfo_button")
        self.setInfo_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #11879C;\n"
"    border-radius: 6px;\n"
"    background-color: #11879C;\n"
"    min-width: 80px;\n"
"	font: 16px;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: #2B587B;\n"
"	border-color: #2B587B;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.setInfo_button)


        self.horizontalLayout_9.addWidget(self.frame)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.reservation_label = QLabel(self.frame_2)
        self.reservation_label.setObjectName(u"reservation_label")

        self.verticalLayout_2.addWidget(self.reservation_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.model_label = QLabel(self.frame_2)
        self.model_label.setObjectName(u"model_label")

        self.horizontalLayout_3.addWidget(self.model_label)

        self.modelLabel = QLabel(self.frame_2)
        self.modelLabel.setObjectName(u"modelLabel")

        self.horizontalLayout_3.addWidget(self.modelLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.price_label = QLabel(self.frame_2)
        self.price_label.setObjectName(u"price_label")

        self.horizontalLayout_4.addWidget(self.price_label)

        self.priceLabel = QLabel(self.frame_2)
        self.priceLabel.setObjectName(u"priceLabel")

        self.horizontalLayout_4.addWidget(self.priceLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.interval_label = QLabel(self.frame_2)
        self.interval_label.setObjectName(u"interval_label")

        self.horizontalLayout_5.addWidget(self.interval_label)

        self.intervalLabel = QLabel(self.frame_2)
        self.intervalLabel.setObjectName(u"intervalLabel")

        self.horizontalLayout_5.addWidget(self.intervalLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.days_label = QLabel(self.frame_2)
        self.days_label.setObjectName(u"days_label")

        self.horizontalLayout_6.addWidget(self.days_label)

        self.totalDayLabel = QLabel(self.frame_2)
        self.totalDayLabel.setObjectName(u"totalDayLabel")

        self.horizontalLayout_6.addWidget(self.totalDayLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.branch_label = QLabel(self.frame_2)
        self.branch_label.setObjectName(u"branch_label")

        self.horizontalLayout_7.addWidget(self.branch_label)

        self.branchLabel = QLabel(self.frame_2)
        self.branchLabel.setObjectName(u"branchLabel")

        self.horizontalLayout_7.addWidget(self.branchLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.totalPrice_label = QLabel(self.frame_2)
        self.totalPrice_label.setObjectName(u"totalPrice_label")

        self.horizontalLayout_8.addWidget(self.totalPrice_label)

        self.totalPriceLabel = QLabel(self.frame_2)
        self.totalPriceLabel.setObjectName(u"totalPriceLabel")

        self.horizontalLayout_8.addWidget(self.totalPriceLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.confirm_button = QPushButton(self.frame_2)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #11879C;\n"
"    border-radius: 6px;\n"
"    background-color: #11879C;\n"
"    min-width: 80px;\n"
"	font: 16px;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: #2B587B;\n"
"	border-color: #2B587B;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.confirm_button)


        self.horizontalLayout_9.addWidget(self.frame_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reservation", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CAR RENTAL RESERVATION", None))
        self.pickup_label.setText(QCoreApplication.translate("MainWindow", u"Pick-up date and time:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Return date and time:", None))
        self.selectBranch_label.setText(QCoreApplication.translate("MainWindow", u"Service branch:", None))
        self.setInfo_button.setText(QCoreApplication.translate("MainWindow", u"Set Info", None))
        self.reservation_label.setText(QCoreApplication.translate("MainWindow", u"RESERVATION INFORMATION", None))
        self.model_label.setText(QCoreApplication.translate("MainWindow", u"car model:", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.price_label.setText(QCoreApplication.translate("MainWindow", u"Price per day:", None))
        self.priceLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.interval_label.setText(QCoreApplication.translate("MainWindow", u"Rental's interval:", None))
        self.intervalLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.days_label.setText(QCoreApplication.translate("MainWindow", u"total days:", None))
        self.totalDayLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.branch_label.setText(QCoreApplication.translate("MainWindow", u"Service branch:", None))
        self.branchLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.totalPrice_label.setText(QCoreApplication.translate("MainWindow", u"Total price:", None))
        self.totalPriceLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.confirm_button.setText(QCoreApplication.translate("MainWindow", u"confirm", None))
    # retranslateUi

