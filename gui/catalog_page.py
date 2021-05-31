# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'catalog_page.ui'
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
        Form.resize(1080, 720)
        Form.setMaximumSize(QSize(1080, 720))
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(31, 95, 139, 255), stop:0.364532 rgba(24, 145, 172, 255), stop:1 rgba(17, 127, 130, 255));\n"
"	padding: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"	background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background: none;\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: white;\n"
"	border: none;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: none;\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	color: #323232;\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     height: 18px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 6px;\n"
"     background-color: grey;   \n"
" }\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: white;\n"
"	border: 1px solid white;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"padding-left: 0px;")

        self.horizontalLayout_4.addWidget(self.label)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 80))
        self.pushButton.setMaximumSize(QSize(80, 80))
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background: none;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	image: url(:/catalog/shopping-cart-white.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: none;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	image: url(:/catalog/shopping-cart.png);\n"
"}")
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setPointSize(28)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: white;\n"
"padding-top: 0px;\n"
"padding-left:  0px;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignTop)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 64))
        self.label_3.setMaximumSize(QSize(16777215, 64))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"padding-left: 0px;")

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignTop)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 50))
        self.comboBox.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setPointSize(18)
        self.comboBox.setFont(font4)

        self.verticalLayout_4.addWidget(self.comboBox, 0, Qt.AlignTop)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 64))
        self.label_4.setMaximumSize(QSize(16777215, 64))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"padding-left: 0px;\n"
"padding-bottom: 1px;\n"
"padding-top: 1px;")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignTop)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 50))
        self.comboBox_2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_4.addWidget(self.comboBox_2, 0, Qt.AlignTop)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 64))
        self.label_5.setMaximumSize(QSize(16777215, 64))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"padding-left: 0px;")

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignTop)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 50))
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 55))
        font5 = QFont()
        font5.setPointSize(18)
        font5.setBold(True)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"padding :1px;")

        self.horizontalLayout.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(820, 580))
        self.scrollArea.setMaximumSize(QSize(820, 580))
        self.scrollArea.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: white;\n"
"	border-radius: 20px;\n"
"}")
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -60, 850, 600))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(850, 600))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(850, 600))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea, 0, Qt.AlignRight)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700; color:#b6b8bc;\">Car</span><span style=\" color:#dfe2e6;\">Rental</span></p></body></html>", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u2630 Filter", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">Brand</span></p></body></html>", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Any", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">Car Type</span></p></body></html>", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Form", u"Any", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">Price</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">TO</span></p></body></html>", None))
    # retranslateUi

