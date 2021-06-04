# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup_page.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import Qt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 580)
        Form.setMinimumSize(QSize(700, 580))
        Form.setMaximumSize(QSize(700, 580))
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(31, 95, 139, 255), stop:0.364532 rgba(24, 145, 172, 255), stop:1 rgba(17, 127, 130, 255));\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(590, 460))
        self.frame.setMaximumSize(QSize(600, 480))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background: white;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #0c7b93;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: none;\n"
"	background-color: white;\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: #0c7b93;\n"
"	border-top: none;\n"
"	border-left: none;\n"
"	border-right: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: white;\n"
"	font: 18px;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	background-color: #0c7b93;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(180, 70))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label)

        self.username_field = QLineEdit(self.frame)
        self.username_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setMaximumSize(QSize(700, 40))

        self.verticalLayout.addWidget(self.username_field)

        self.email_field = QLineEdit(self.frame)
        self.email_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.email_field.setObjectName(u"email_field")
        self.email_field.setMaximumSize(QSize(700, 40))

        self.verticalLayout.addWidget(self.email_field)

        self.contact_field = QLineEdit(self.frame)
        self.contact_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.contact_field.setObjectName(u"contact_field")
        self.contact_field.setMaximumSize(QSize(700, 40))

        self.verticalLayout.addWidget(self.contact_field)

        self.card_field = QLineEdit(self.frame)
        self.card_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.card_field.setObjectName(u"card_field")
        self.card_field.setMaximumSize(QSize(700, 40))

        self.verticalLayout.addWidget(self.card_field)

        self.password_field = QLineEdit(self.frame)
        self.password_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setMaximumSize(QSize(700, 40))
        self.password_field.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_field)

        self.confirmPass_field = QLineEdit(self.frame)
        self.confirmPass_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.confirmPass_field.setObjectName(u"confirmPass_field")
        self.confirmPass_field.setMaximumSize(QSize(700, 40))
        self.confirmPass_field.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.confirmPass_field)

        self.signup_button = QPushButton(self.frame)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setMinimumSize(QSize(150, 50))
        self.signup_button.setMaximumSize(QSize(150, 50))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.signup_button.setFont(font1)
        self.signup_button.setStyleSheet(u"QPushButton:pressed {\n"
"	background: none;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #0C5A76, stop: 1 #0c7b93);\n"
"}")

        self.verticalLayout.addWidget(self.signup_button, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.username_field.setText("")
        self.username_field.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.email_field.setText("")
        self.email_field.setPlaceholderText(QCoreApplication.translate("Form", u"E-mail", None))
        self.contact_field.setText("")
        self.contact_field.setPlaceholderText(QCoreApplication.translate("Form", u"Contact", None))
        self.card_field.setText("")
        self.card_field.setPlaceholderText(QCoreApplication.translate("Form", u"Credit Card Number", None))
        self.password_field.setText("")
        self.password_field.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.confirmPass_field.setText("")
        self.confirmPass_field.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.signup_button.setText(QCoreApplication.translate("Form", u"Sign Up", None))
    # retranslateUi

