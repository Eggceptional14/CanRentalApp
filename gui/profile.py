import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from gui.link.profile_ui import Ui_Form
from gui.car_history import CarHistory
from src.profile import Profile


class ProfileUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.rentHsBtn.clicked.connect(self.showHistory)
        self.user = ""
        self.profile = Profile()
        self.history = CarHistory()

    def setUser(self, user):
        self.user = user
        self.profile.loadData(self.user)

    def setInfo(self):
        self.ui.uNameLabel.setText(self.profile.uName)
        self.ui.nameLabel.setText(self.profile.name)
        self.ui.emailLabel.setText(self.profile.email)
        self.ui.contactLabel.setText(self.profile.contact)
        self.ui.cardLabel.setText(self.profile.credCard)

    def showHistory(self):
        self.history.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Profile()
    w.setAttribute(Qt.WA_StyledBackground)
    w.show()
    sys.exit(app.exec_())