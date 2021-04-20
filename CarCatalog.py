class CarCatalog:
    def __init__(self):
        self.carList = []

    def addCar(self, car):
        self.carList.append(car)

    def deleteCar(self, car):
        self.carList.remove(car)

    def displayCar(self):
        for i in self.carList:
            print(i)