import math

class Circle:
    def __init__(self, posX, posY, radius):
        self.posX = posX
        self.posY = posY
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return self.radius * 2
    
    def length(self):
        return math.pi * self.radius * 2

        
        


