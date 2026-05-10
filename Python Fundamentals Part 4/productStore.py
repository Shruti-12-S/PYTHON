'''
Design and create an online store for Products (name,price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.
'''

class Product:

    count = 0

    def __init__(self,name,price):
        self.name =name
        self.price=price
        Product.count+=1

    def get_info(self):#instance method
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price,percentage):
        print(f"Discounted price = {price - (price*percentage/100)}")

p1 = Product("phone", 10000)
p2 = Product("Laptop",50000)
p3 = Product("pen", 10)
p4= Product("charger",250)

p1.get_info()
Product.get_count()
p1.calc_discount(10000,10)
p2.calc_discount(p2.price,5)