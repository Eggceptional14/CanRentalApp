import sqlite3
from sqlite3 import Error


class Profile:
    def __init__(self):
        self.name = ""
        self.uName = ""
        self.email = ""
        self.credcard = ""
        