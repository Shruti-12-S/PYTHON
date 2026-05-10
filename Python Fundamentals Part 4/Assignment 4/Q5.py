'''
Concept: Inheritance
Create a base class Vehicle with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes - seats (in Car) & engine_cc(in Bike).
'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print("Brand: ", self.brand)
        print("Model: ",self.model)

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats =seats

    def display_car(self):
        self.display_vehicle()
        print("Seats: ",self.seats)

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_bike(self):
        self.display_vehicle()
        print("Engine CC: ", self.engine_cc)

c1 = Car("Toyota", "Fortuner", 7)
b1 = Bike("Royal Enfield", "Classic 350", 350)

# Display details
print("Car Details")
c1.display_car()

print("\nBike Details")
b1.display_bike()