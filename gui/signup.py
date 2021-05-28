import sys
import re
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from gui.signup_page import Ui_Form

import sqlite3
from sqlite3 import Error

class Signup(QWidget):

    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.missingField = []

        self.ui.signup_button.clicked.connect(self.signup)

    def signup(self):
        missing_field = ""
        if self.existText(self.ui.username_field.text()) is False:
            missing_field += "Username\n"
        if self.existText(self.ui.password_field.text()) is False:
            missing_field += "Password\n"
        if self.existText(self.ui.email_field.text()) is False:
            missing_field += "Email\n"
        if self.existText(self.ui.contact_field.text()) is False:
            missing_field += "Contact\n"
        if self.existText(self.ui.card_field.text()) is False:
            missing_field += "Credit Card\n"

        if len(missing_field) != 0:
            self.showdialog("Information is missing: ", missing_field)
        else:
            warning_message = ""
            if self.validateUsername() is False:
                warning_message += "Username already exists.\n"
            if self.validatePassword() is False:
                warning_message += "Passwords are not matched/Password needs to be more than 6 letters.\n"
            if self.validateEmail() is False:
                warning_message += "Email address is invalid.\n"
            if self.validateContact() is False:
                warning_message += "Contact information is invalid.\n"
            if self.validateCreditCard() is False:
                warning_message += "Credit card information is invalid.\n"
            
            if len(warning_message) != 0:
                self.showdialog("There was an error in your input. Please try again.", warning_message)
            else:
                self.createUser(self.ui.username_field.text(), self.ui.password_field.text(), self.ui.email_field.text(), self.ui.contact_field.text(), self.ui.card_field.text())
                self.close()
    
    def validateUsername(self):
        name = self.ui.username_field.text()

        conn = None
        try:
            conn = sqlite3.connect("../db/userInfo.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM userInformation WHERE userName=?", (name,))
            rows = cur.fetchall()
            # enter invalid username
            if len(rows) != 0:
                return False
        except Error as e:
            print(e)
            return True

        conn.close()
    
    def validatePassword(self):
        return self.ui.password_field.text() == self.ui.confirmPass_field.text() and len(self.ui.password_field.text()) >= 6

    def validateEmail(self):
        return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", self.ui.email_field.text()))

    def validateContact(self):
        return (self.ui.contact_field.text()).isnumeric

    def validateCreditCard(self):
        return (self.ui.card_field.text()).isnumeric
    
    def existText(self, text):
        if text:
            print("True")
            return True
        print("False")
        return False
    
    def createUser(self, username, password, email, contact, creditCard):
        try:
            sqliteConnection = sqlite3.connect("../db/userInfo.db")
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO userInformation
                            (userName, password, email, contact, creditCard) 
                            VALUES (?, ?, ?, ?, ?);"""

            data_tuple = (username, password, email, contact, creditCard)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Inserted successfully")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def showdialog(self, warning_message, warning_addition):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Warning:")
        msg.setInformativeText(warning_message)
        msg.setWindowTitle("MessageBox")
        msg.setDetailedText(warning_addition)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Signup()
    w.show()
    sys.exit(app.exec_())