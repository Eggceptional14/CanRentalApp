# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'car_description.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_CarDescription(object):
    def setupUi(self, CarDescription):
        if not CarDescription.objectName():
            CarDescription.setObjectName(u"CarDescription")
        CarDescription.resize(390, 490)
        CarDescription.setMinimumSize(QSize(390, 490))
        CarDescription.setMaximumSize(QSize(390, 490))
        CarDescription.setStyleSheet(u"QFrame{\n"
"	background: grey;\n"
"	border: 1px solid grey;\n"
"	border-radius: 30px;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #323232;\n"
"}")
        self.verticalLayout = QVBoxLayout(CarDescription)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(CarDescription)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(370, 470))
        self.frame.setMaximumSize(QSize(370, 470))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(350, 210))
        self.label.setMaximumSize(QSize(350, 210))

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 30))
        self.label_2.setMaximumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.label_2)

        self.brandLabel = QLabel(self.frame)
        self.brandLabel.setObjectName(u"brandLabel")
        self.brandLabel.setMinimumSize(QSize(0, 30))
        self.brandLabel.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.brandLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 30))
        self.label_3.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.modelLabel = QLabel(self.frame)
        self.modelLabel.setObjectName(u"modelLabel")
        self.modelLabel.setMinimumSize(QSize(0, 30))
        self.modelLabel.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.modelLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 30))
        self.label_4.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.typeLabel = QLabel(self.frame)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setMinimumSize(QSize(0, 30))
        self.typeLabel.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.typeLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.pphLabel = QLabel(self.frame)
        self.pphLabel.setObjectName(u"pphLabel")
        self.pphLabel.setMinimumSize(QSize(0, 30))
        self.pphLabel.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.pphLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.rentButton = QPushButton(self.frame)
        self.rentButton.setObjectName(u"rentButton")
        self.rentButton.setMinimumSize(QSize(140, 50))
        self.rentButton.setMaximumSize(QSize(140, 50))
        self.rentButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: #323232;\n"
"	border-color: grey;\n"
"	border-radius: 10px;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"	background-color: #232323;\n"
"	border-color: grey;\n"
"	border-radius: 10px;\n"
"	padding: 0px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.rentButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(CarDescription)

        QMetaObject.connectSlotsByName(CarDescription)
    # setupUi

    def retranslateUi(self, CarDescription):
        CarDescription.setWindowTitle(QCoreApplication.translate("CarDescription", u"Form", None))
        self.label.setText(QCoreApplication.translate("CarDescription", u"Picture", None))
        self.label_2.setText(QCoreApplication.translate("CarDescription", u"Brand", None))
        self.brandLabel.setText(QCoreApplication.translate("CarDescription", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("CarDescription", u"Model", None))
        self.modelLabel.setText(QCoreApplication.translate("CarDescription", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("CarDescription", u"Type", None))
        self.typeLabel.setText(QCoreApplication.translate("CarDescription", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("CarDescription", u"Price Per Hour", None))
        self.pphLabel.setText(QCoreApplication.translate("CarDescription", u"TextLabel", None))
        self.rentButton.setText(QCoreApplication.translate("CarDescription", u"Rent This Car", None))
    # retranslateUi

