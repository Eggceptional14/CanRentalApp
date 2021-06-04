class CarItem:
    def __init__(self, image, brand, carId, model,carType, price):
        self.image = image
        self.brand = brand
        self.carId = carId
        self.model = model
        self.carType = carType
        self.price = price
    
    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = image

    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    def getCarId(self):
        return self.carId

    def setCarId(self, carId):
        self.carId = carId

    def getCarModel(self):
        return self.model

    def setCarModel(self, model):
        self.model = model

    def getCarType(self):
        return self.carType

    def setcarType(self, carType):
        self.carType = carType

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    
    def __str__(self):
        return f'Car: {self.brand}, { self.model} Price: {self.price}'



    
    