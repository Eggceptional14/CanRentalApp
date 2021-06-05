# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_page.ui'
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
        Form.resize(470, 370)
        Form.setMinimumSize(QSize(470, 370))
        Form.setMaximumSize(QSize(470, 370))
        Form.setStyleSheet(u"QWidget {\n"
"	background-image: url(:/login/login_background.png);\n"
"	background-color: transparent;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"	background: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font-weight: bold;\n"
"	background: white;\n"
"	border: 2px;\n"
"	border-radius: 10px;\n"
"	color: #1D9AAE;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color: white;\n"
"	background-color: grey;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(50, 16777215))
        self.label_10.setStyleSheet(u"image: url(:/catalog/user-white.png);\n"
"padding: 0px;\n"
"border: none;\n"
"margin: 0px;")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	font: 24px;\n"
"	font-weight: bold;\n"
"	padding-left: 5px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(90, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font-weight: bold;\n"
"")

        self.horizontalLayout.addWidget(self.label)

        self.nameLabel = QLabel(Form)
        self.nameLabel.setObjectName(u"nameLabel")
        font2 = QFont()
        font2.setPointSize(14)
        self.nameLabel.setFont(font2)

        self.horizontalLayout.addWidget(self.nameLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(90, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.uNameLabel = QLabel(Form)
        self.uNameLabel.setObjectName(u"uNameLabel")
        self.uNameLabel.setFont(font2)

        self.horizontalLayout_2.addWidget(self.uNameLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(90, 16777215))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.emailLabel = QLabel(Form)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setFont(font2)

        self.horizontalLayout_3.addWidget(self.emailLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(90, 16777215))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.contactLabel = QLabel(Form)
        self.contactLabel.setObjectName(u"contactLabel")
        self.contactLabel.setFont(font2)

        self.horizontalLayout_7.addWidget(self.contactLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(90, 16777215))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.cardLabel = QLabel(Form)
        self.cardLabel.setObjectName(u"cardLabel")
        self.cardLabel.setFont(font2)

        self.horizontalLayout_4.addWidget(self.cardLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.rentHsBtn = QPushButton(Form)
        self.rentHsBtn.setObjectName(u"rentHsBtn")
        self.rentHsBtn.setMinimumSize(QSize(0, 30))
        self.rentHsBtn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.rentHsBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Your Profile", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.nameLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Username", None))
        self.uNameLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Email", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Contact", None))
        self.contactLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Credit Card", None))
        self.cardLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.rentHsBtn.setText(QCoreApplication.translate("Form", u"Rent History", None))
    # retranslateUi

