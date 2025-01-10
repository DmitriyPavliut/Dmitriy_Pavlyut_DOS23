import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius