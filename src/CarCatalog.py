import sqlite3
from sqlite3 import Error

from src.CarItem import CarItem


class CarCatalog:
    def __init__(self):
        self.carList = []
        self.loadData()

    def loadData(self):
        try:
            sqliteConnection = sqlite3.connect("../db/rentalCar.db")
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

    def getBrandList(self):
        brand = set()
        try:
            sqliteConnection = sqlite3.connect("../db/rentalCar.db")
            print("Connected to SQLite")

            sqlite_select_query = "SELECT * from carCatalog"
            result = sqliteConnection.execute(sqlite_select_query)
            for row in result:
                # print(row)
                brand.add(row[2])

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return brand

    def getCarTypeList(self):
        carType = set()

        try:
            sqliteConnection = sqlite3.connect("../db/rentalCar.db")
            print("Connected to SQLite")

            sqlite_select_query = "SELECT * from carCatalog"
            result = sqliteConnection.execute(sqlite_select_query)
            for row in result:
                # print(row)
                carType.add(row[4])

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return carType

    def deleteCar(self, car):
        self.carList.remove(car)

    def displayCar(self):
        for i in self.carList:
            print(i)

    def brandFilter(self, carFilter):
        carList = set()
        if carFilter == "Any":
            carList = set(self.carList)
        for car in self.carList:
            if carFilter == car.getBrand():
                carList.add(car)
        return carList

    def typeFilter(self, carFilter):
        carList = set()
        if carFilter == "Any":
            carList = set(self.carList)
        for car in self.carList:
            if carFilter == car.getCarType():
                carList.add(car)
        return carList

    def setPriceRange(self, priceRange):
        carList = set()
        for car in self.carList:
            if priceRange[0] < car.getPrice() < priceRange[1]:
                carList.add(car)
        return carList

if __name__ == '__main__':
    c = CarCatalog()
    c.displayCar()
    print(c.getBrandList())
    print(c.getCarTypeList())