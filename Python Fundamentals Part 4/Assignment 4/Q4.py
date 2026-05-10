'''
Concept: Function Overriding
Create a class Shape with a method area().
Create subclasses Circle, Rectangle and Triangle that override the area() method.
'''

class Shape:
    def area(self):
        print("Area method should be overridden in subclasses")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5*self.base*self.height


r = Rectangle(10,5)
c = Circle(7)
t = Triangle(8,6)

# Displaying areas
print("Area of Rectangle:", r.area())
print("Area of Circle:", c.area())
print("Area of Triangle:", t.area())