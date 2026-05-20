from cart import *

product1 = Product("Washing machine", 1000)
product2 = Product("Flashlight", 1500 )

tv1 = TV("Sony Bravia", 2000, "55\"")
tv2 = TV("LG TV", 1000, "49\"")

phone1 = Phone("Samsung Galaxy", 800, "Black")
phone2 = Phone("Sony Xperia", 500, "Purple")

cart = Cart()

cart.addProduct(product1)
cart.addProduct(product2)

cart.addProduct(tv1)
cart.addProduct(tv2)

cart.addProduct(phone1)
cart.addProduct(phone2)

print(cart)
