import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from mainWindow import MainWindow


import sqlite3
from sqlite3 import Error

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = MainWindow()
    
    def run(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())

app = Application()
app.run()