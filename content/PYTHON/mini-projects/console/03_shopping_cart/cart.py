from products import *

class Cart:
    def __init__(self):
        self.__productList = []
        self.__cartValue = 0

    def addProduct(self, product):
        if isinstance(product, Product):
            self.__productList.append(product)
            self.calculateCartValue()

    def calculateCartValue(self):
        self.__cartValue = 0
        for product in self.__productList:
            self.__cartValue += product.price

    def __str__(self):
        cartInfo = "Cart Products:\n\n"
        for product in self.__productList:
            cartInfo += f"ProductID:{product.productID}\n - Name: {product.name}\n - Price: {product.price}\n"
        cartInfo += f"\nCart total Price: {self.__cartValue}\n"
        return cartInfo
