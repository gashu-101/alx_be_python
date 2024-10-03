import math

# Base class Shape
class Shape:
    def area(self):
        """Method to calculate the area. To be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement this method")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate the rectangle's area."""
        return self.length * self.width

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize a circle with radius."""
        self.radius = radius

    def area(self):
        """Override area method to calculate the circle's area."""
        return math.pi * (self.radius ** 2)
