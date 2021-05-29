import sqlite3
from sqlite3 import Error

from src.CarItem import CarItem


class CarCatalog:
    def __init__(self):
        self.carList = []
        self.loadData()

    def loadData(self):
        try:
            sqliteConnection = sqlite3.connect("../db/carCatalog.db")
            print("Connected to SQLite")

            sqlite_select_query = "SELECT * from carCatalog"
            result = sqliteConnection.execute(sqlite_select_query)
            for row in result:
                # print(row)
                image, brand, id, model, carClass, pph, available = row[0], row[2], row[1], row[3], row[4], row[5], row[6]
                car = CarItem(image, brand, id, model, carClass, pph, available)
                self.addCar(car)

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def getList(self):
        return self.carList

    def addCar(self, car):
        self.carList.append(car)

    def deleteCar(self, car):
        self.carList.remove(car)

    def displayCar(self):
        for i in self.carList:
            print(i)


if __name__ == '__main__':
    c = CarCatalog()
    c.displayCar()