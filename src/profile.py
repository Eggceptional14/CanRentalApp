import sqlite3
from sqlite3 import Error


class Profile:
    def __init__(self):
        self.name = ""
        self.uName = ""
        self.email = ""
        self.contact = ""
        self.credCard = ""

    def loadData(self, uName):
        self.uName = uName
        try:
            sqliteConnection = sqlite3.connect("../db/rentalCar.db")
            print("Connected to SQLite")
            cur = sqliteConnection.cursor()
            cur.execute("SELECT * FROM userInformation WHERE userName=?", (uName,))
            rows = cur.fetchall()
            row = rows[0]
            name, email, contact, cred = row[1], row[3], row[4], row[5]
            self.name = name
            self.email = email
            self.contact = contact
            self.credCard = cred

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")