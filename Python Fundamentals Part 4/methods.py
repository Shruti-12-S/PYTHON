class Laptop:
    storage_type = "SSD" #class variable

    def __init__(self,RAM,storage):#instance method
        self.RAM = RAM
        self.storage = storage
    
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage} storage {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price -(discount*price/100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16gb","512gb")


# fnx => (price, discount)=>final price static methods
l1.calc_discount(40000,10)

