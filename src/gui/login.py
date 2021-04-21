import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from login_page import Ui_login_widget

class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_login_widget()
        self.ui.setupUi(self)
        self.ui.signin_button.clicked.connect(self.activate)

    def activate(self):
        print("Hello")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    sys.exit(app.exec_())

