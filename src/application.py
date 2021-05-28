import sys
from PySide6.QtWidgets import *
from src.mainWindow import MainWindow


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = MainWindow()
    
    def run(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())

app = Application()
app.run()