# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checkout_page.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import assets.images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 500)
        Form.setMaximumSize(QSize(700, 500))
        Form.setStyleSheet(u"QWidget {\n"
"	background-image: url(:/login/login_background.png);\n"
"	background-repeat: no-repeat;\n"
"}	\n"
"\n"
"QLabel {\n"
"	background: none;\n"
"	color: white;\n"
"	font: 14px;\n"
"}	\n"
"\n"
"QLineEdit {\n"
"	background: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background: none;\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background: none;\n"
"	background-color: grey;\n"
"	color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 16777215))
        self.label_2.setStyleSheet(u"image: url(:/catalog/shopping-cart-white.png);")

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 24px;\n"
"font-weight: bold;\n"
"padding-left: 5px;")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 16px;\n"
"font-weight: bold;")

        self.verticalLayout_6.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(50, 16777215))
        self.label_7.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 16777215))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.modelLabel = QLabel(Form)
        self.modelLabel.setObjectName(u"modelLabel")

        self.gridLayout.addWidget(self.modelLabel, 1, 1, 1, 1)

        self.brandLabel = QLabel(Form)
        self.brandLabel.setObjectName(u"brandLabel")

        self.gridLayout.addWidget(self.brandLabel, 0, 1, 1, 1)

        self.typeLabel = QLabel(Form)
        self.typeLabel.setObjectName(u"typeLabel")

        self.gridLayout.addWidget(self.typeLabel, 0, 3, 1, 1)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(100, 16777215))
        self.label_12.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)

        self.priceLabel = QLabel(Form)
        self.priceLabel.setObjectName(u"priceLabel")

        self.gridLayout.addWidget(self.priceLabel, 1, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font-weight: bold;\n"
"margin-bottom: 0px;")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.startInput = QLineEdit(Form)
        self.startInput.setObjectName(u"startInput")
        self.startInput.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.startInput)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.endInput = QLineEdit(Form)
        self.endInput.setObjectName(u"endInput")
        self.endInput.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.endInput)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.checkoutBtn = QPushButton(Form)
        self.checkoutBtn.setObjectName(u"checkoutBtn")
        self.checkoutBtn.setMinimumSize(QSize(150, 40))
        self.checkoutBtn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.checkoutBtn, 0, Qt.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Checkout", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Car", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Type", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Model", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Brand", None))
        self.modelLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.brandLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.typeLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Price Per Day", None))
        self.priceLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Start Date", None))
        self.startInput.setPlaceholderText(QCoreApplication.translate("Form", u"input format: DDMMYYYY", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"End Date", None))
        self.endInput.setPlaceholderText(QCoreApplication.translate("Form", u"input format: DDMMYYYY", None))
        self.checkoutBtn.setText(QCoreApplication.translate("Form", u"Checkout", None))
    # retranslateUi

