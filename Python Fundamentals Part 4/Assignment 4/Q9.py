'''
concept: Multiple Inheritance
Create the following classes: Herbivore, Carnivore, Omnivore with some attributes & methods.
Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.
'''


# Class Herbivore
class Herbivore:
    def eat_plants(self):
        print("Herbivore eats plants.")


# Class Carnivore
class Carnivore:
    def eat_meat(self):
        print("Carnivore eats meat.")


# Class Omnivore
class Omnivore:
    def eat_both(self):
        print("Omnivore eats both plants and meat.")


# Bear class inheriting from all classes
class Bear(Herbivore, Carnivore, Omnivore):

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Bear Name:", self.name)


# Creating object
b1 = Bear("Brown Bear")

# Display details
b1.display()

# Accessing methods from multiple parent classes
b1.eat_plants()
b1.eat_meat()
b1.eat_both()

