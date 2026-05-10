'''
Concept:Constructor Overloading(with Default Parameters)
Create a class Person that allows the constructor to work with:
    • name only
    • name+age
    • name+age+address
As direct constructor overloading(multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.
'''

class Person:
    def __init__(self,name,age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name: ",self.name)

        if self.age is not None:
            print("Age : ",self.age)
        
        if self.address is not None:
            print("Address :", self.address)

        print()


# Object with name only
p1 = Person("Rahul")

# Object with name and age
p2 = Person("Aman", 22)

# Object with name, age, and address
p3 = Person("Priya", 21, "Pune")

# Display details
p1.display()
p2.display()
p3.display()