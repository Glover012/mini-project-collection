import random

class Product:
    productUsedIDs = []
    productList = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.productID = self.getProductID()
        self.productList.append(self)

    def __str__(self):
        return f"ProductID:{self.productID}\n - Name: {self.name}\n - Price: {self.price}\n"

    def getProductID(self):
        ID = random.randrange(1000, 9999, 1) 
        while ID in self.productUsedIDs:
            ID = random.randrange(1000, 9999, 1)
        self.productUsedIDs.append(int(ID))
        return int(ID)

    def printProducts(self):
        print("Product list: \n")
        for product in self.productList:
            print(product.__str__())

    def printUsedIDs(self):
        i = 0
        for usedID in self.productUsedIDs:
            print(f"{i} - {usedID}")
            i += 1

class TV(Product):
    tvList = []

    def __init__(self, name, price, width):
        super().__init__(name, price)
        self.width = width
        self.tvList.append(self)

    def __str__(self): 
        return super().__str__() + f" - Width: {self.width}\n"
    
    def printTVs(self):
        for tv in self.tvList:
            print(tv.__str__())

class Phone(Product):
    phoneList = []

    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color
        self.phoneList.append(self)

    def __str__(self):
        return super().__str__() + f" - Color: {self.color}\n"

    def printPhones(self):
        for phone in self.phoneList:
            print(phone.__str__())
