import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from login import Login
from signup import Signup

import sqlite3
from sqlite3 import Error

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.login = Login()
        self.login.ui.signup_button.clicked.connect(self.register)
        self.setCentralWidget(self.login)
        self.signup = Signup()
    
    def register(self):
        self.signup.show()
